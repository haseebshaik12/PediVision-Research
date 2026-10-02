from pathlib import Path
import argparse

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


def load_dataset(file_path):
    """Load a prepared clinical feature dataset."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def train_clinical_model(
    train_file,
    feature_columns,
    label_column,
):
    """Train a clinical-only logistic-regression baseline."""

    data = load_dataset(train_file)

    missing_columns = [
        column
        for column in feature_columns + [label_column]
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    X = data[feature_columns]
    y = data[label_column]

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    random_state=42,
                ),
            ),
        ]
    )

    model.fit(X, y)

    predictions = model.predict(X)

    accuracy = accuracy_score(y, predictions)

    print("\n=== PediVision Clinical Baseline Model ===")
    print(f"Training records: {len(data)}")
    print(f"Features used: {feature_columns}")
    print(f"Target column: {label_column}")
    print(f"Training accuracy: {accuracy:.4f}")

    print(
        "\nNote: This accuracy is training-set performance "
        "and is not a final research result."
    )

    print("\nClinical baseline model training completed.")

    return model


def main():
    parser = argparse.ArgumentParser(
        description="Train a clinical-only baseline classifier."
    )

    parser.add_argument(
        "train_file",
        help="Training clinical feature CSV",
    )

    parser.add_argument(
        "--features",
        nargs="+",
        required=True,
        help="Clinical feature column names",
    )

    parser.add_argument(
        "--label",
        required=True,
        help="Target label column",
    )

    args = parser.parse_args()

    try:
        train_clinical_model(
            args.train_file,
            args.features,
            args.label,
        )

    except Exception as error:
        print(f"\nError training clinical baseline: {error}")


if __name__ == "__main__":
    main()