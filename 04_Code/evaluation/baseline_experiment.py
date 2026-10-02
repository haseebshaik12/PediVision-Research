from pathlib import Path
import argparse

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


def load_dataset(file_path):
    """Load a prepared classification dataset."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def evaluate_predictions(y_true, y_pred):
    """Calculate basic classification evaluation metrics."""

    accuracy = accuracy_score(y_true, y_pred)

    print("\n=== PediVision Baseline Evaluation ===")
    print(f"Accuracy: {accuracy:.4f}")

    print("\n=== Classification Report ===")
    print(
        classification_report(
            y_true,
            y_pred,
            zero_division=0,
        )
    )

    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_true, y_pred))

    return accuracy


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate PediVision classification predictions."
    )

    parser.add_argument(
        "file_path",
        help="CSV containing true and predicted labels",
    )

    parser.add_argument(
        "--true-label",
        default="true_label",
        help="Column containing the true labels",
    )

    parser.add_argument(
        "--predicted-label",
        default="predicted_label",
        help="Column containing predicted labels",
    )

    args = parser.parse_args()

    try:
        data = load_dataset(args.file_path)

        if args.true_label not in data.columns:
            raise ValueError(
                f"True-label column '{args.true_label}' not found."
            )

        if args.predicted_label not in data.columns:
            raise ValueError(
                f"Predicted-label column '{args.predicted_label}' not found."
            )

        evaluate_predictions(
            data[args.true_label],
            data[args.predicted_label],
        )

        print("\nBaseline evaluation completed.")

    except Exception as error:
        print(f"\nError evaluating predictions: {error}")


if __name__ == "__main__":
    main()