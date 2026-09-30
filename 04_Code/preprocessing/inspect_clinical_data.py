from pathlib import Path
import argparse

import pandas as pd


def inspect_clinical_data(file_path):
    """Inspect a clinical CSV file without assuming specific variables."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() != ".csv":
        raise ValueError("Expected a CSV file.")

    data = pd.read_csv(file_path)

    print("\n=== PediVision Clinical Data Inspection ===")
    print(f"File: {file_path.name}")
    print(f"Rows: {data.shape[0]}")
    print(f"Columns: {data.shape[1]}")

    print("\n=== Columns ===")

    for column in data.columns:
        print(f"- {column}")

    print("\n=== Data Types ===")
    print(data.dtypes.to_string())

    print("\n=== Missing Values ===")
    missing_values = data.isnull().sum()

    for column, count in missing_values.items():
        print(f"- {column}: {count}")

    print("\n=== Preview ===")
    print(data.head().to_string(index=False))

    print("\nClinical data inspection completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a PediVision clinical CSV file."
    )

    parser.add_argument(
        "file_path",
        help="Path to the clinical CSV file"
    )

    args = parser.parse_args()

    try:
        inspect_clinical_data(args.file_path)

    except Exception as error:
        print(f"\nError inspecting clinical data: {error}")


if __name__ == "__main__":
    main()