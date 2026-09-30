from pathlib import Path
import argparse

import pandas as pd


def inspect_labels(file_path, label_column):
    """Inspect the distribution of a verified dataset label column."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}"
        )

    data = pd.read_csv(file_path)

    if label_column not in data.columns:
        raise ValueError(
            f"Label column '{label_column}' was not found.\n"
            f"Available columns: {list(data.columns)}"
        )

    labels = data[label_column]

    print("\n=== PediVision Label Inspection ===")
    print(f"File: {file_path.name}")
    print(f"Label column: {label_column}")
    print(f"Total records: {len(data)}")
    print(f"Missing labels: {labels.isna().sum()}")
    print(f"Unique labels: {labels.nunique(dropna=True)}")

    print("\n=== Label Distribution ===")

    distribution = labels.value_counts(dropna=False)

    for label, count in distribution.items():
        print(f"- {label}: {count}")

    print("\nLabel inspection completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Inspect classification labels in a PediVision dataset."
    )

    parser.add_argument(
        "file_path",
        help="Path to the dataset CSV",
    )

    parser.add_argument(
        "label_column",
        help="Name of the verified target-label column",
    )

    args = parser.parse_args()

    try:
        inspect_labels(
            args.file_path,
            args.label_column,
        )

    except Exception as error:
        print(f"\nError inspecting labels: {error}")


if __name__ == "__main__":
    main()