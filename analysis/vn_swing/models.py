"""Classical ML models for swing-win classification (scikit-learn + XGBoost)."""
from __future__ import annotations

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_models() -> dict:
    models = {
        "LogReg": Pipeline([
            ("sc", StandardScaler()),
            ("clf", LogisticRegression(max_iter=2000, class_weight="balanced", C=0.5)),
        ]),
        "RandomForest": RandomForestClassifier(
            n_estimators=400, max_depth=6, min_samples_leaf=50,
            class_weight="balanced", random_state=42, n_jobs=-1,
        ),
        "GradBoost": GradientBoostingClassifier(
            n_estimators=300, max_depth=3, learning_rate=0.03, subsample=0.8, random_state=42,
        ),
    }
    try:
        from xgboost import XGBClassifier

        models["XGBoost"] = XGBClassifier(
            n_estimators=400, max_depth=4, learning_rate=0.03, subsample=0.8,
            colsample_bytree=0.8, reg_lambda=1.0, random_state=42, n_jobs=-1,
            eval_metric="logloss",
        )
    except Exception as e:  # noqa: BLE001
        print("  (xgboost unavailable:", e, ")")
    return models


def fit_predict(model, X_tr, y_tr, X_te) -> np.ndarray:
    model.fit(X_tr, y_tr)
    return model.predict_proba(X_te)[:, 1]
