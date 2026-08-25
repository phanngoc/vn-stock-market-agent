"""PyTorch LSTM sequence classifier for swing-win prediction.

Each sample is a window of the last L days of features (info up to day t) used to
predict the triple-barrier label at day t. Standardization stats come from the
training window only (no look-ahead). CPU-friendly (small net, few epochs).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from .features import FEATURE_COLS

torch.manual_seed(42)
np.random.seed(42)


class LSTMClassifier(nn.Module):
    def __init__(self, n_features: int, hidden: int = 32, layers: int = 1, dropout: float = 0.1):
        super().__init__()
        self.lstm = nn.LSTM(n_features, hidden, num_layers=layers, batch_first=True,
                            dropout=dropout if layers > 1 else 0.0)
        self.head = nn.Sequential(nn.Dropout(dropout), nn.Linear(hidden, 1))

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.head(out[:, -1, :]).squeeze(-1)


def _make_sequences(feat_ok: pd.DataFrame, L: int, test_start: str):
    """Build (train, test, latest) sequence sets from the feature panel."""
    tr_X, tr_y = [], []
    te_X, te_meta = [], []
    lt_X, lt_meta = [], []
    for sym, sub in feat_ok.groupby("symbol"):
        sub = sub.sort_values("date").reset_index(drop=True)
        arr = sub[FEATURE_COLS].to_numpy(float)
        for i in range(L - 1, len(sub)):
            seq = arr[i - L + 1 : i + 1]
            row = sub.iloc[i]
            if i == len(sub) - 1:  # latest available window per symbol -> live scoring
                lt_X.append(seq)
                lt_meta.append((row["symbol"], row["date"], row["close"]))
            if pd.isna(row["label"]):
                continue
            if row["date"] < pd.Timestamp(test_start):
                tr_X.append(seq); tr_y.append(row["label"])
            else:
                te_X.append(seq)
                te_meta.append((row["symbol"], row["date"]))
    return (
        np.asarray(tr_X, np.float32), np.asarray(tr_y, np.float32),
        np.asarray(te_X, np.float32), pd.DataFrame(te_meta, columns=["symbol", "date"]),
        np.asarray(lt_X, np.float32), pd.DataFrame(lt_meta, columns=["symbol", "date", "close"]),
    )


def train_lstm(feat_ok: pd.DataFrame, test_start: str, L: int = 20, epochs: int = 12, batch: int = 256):
    Xtr, ytr, Xte, te_meta, Xlt, lt_meta = _make_sequences(feat_ok, L, test_start)
    if len(Xtr) == 0 or len(Xte) == 0:
        raise RuntimeError("not enough sequences")

    # standardize using train stats
    mu = Xtr.reshape(-1, Xtr.shape[-1]).mean(0)
    sd = Xtr.reshape(-1, Xtr.shape[-1]).std(0) + 1e-8
    norm = lambda a: (a - mu) / sd
    Xtr, Xte, Xlt = norm(Xtr), norm(Xte), norm(Xlt)

    dev = torch.device("cpu")
    model = LSTMClassifier(Xtr.shape[-1]).to(dev)
    pos = float(ytr.mean())
    pos_weight = torch.tensor([(1 - pos) / max(pos, 1e-3)], device=dev)
    lossf = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-5)

    Xtr_t = torch.tensor(Xtr); ytr_t = torch.tensor(ytr)
    n = len(Xtr_t)
    for ep in range(epochs):
        model.train()
        perm = torch.randperm(n)
        tot = 0.0
        for s in range(0, n, batch):
            idx = perm[s : s + batch]
            opt.zero_grad()
            logit = model(Xtr_t[idx])
            loss = lossf(logit, ytr_t[idx])
            loss.backward()
            opt.step()
            tot += float(loss) * len(idx)
        if ep == 0 or (ep + 1) % 4 == 0:
            print(f"    LSTM epoch {ep+1}/{epochs} loss={tot/n:.4f}")

    model.eval()
    with torch.no_grad():
        te_prob = torch.sigmoid(model(torch.tensor(Xte))).numpy()
        lt_prob = torch.sigmoid(model(torch.tensor(Xlt))).numpy()
    te_out = te_meta.copy(); te_out["prob"] = te_prob
    lt_out = lt_meta.copy(); lt_out["prob"] = lt_prob
    return te_out, lt_out
