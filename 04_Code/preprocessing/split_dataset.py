from pathlib import Path
import argparse

import pandas as pd
from sklearn.model_selection import train_test_split


def load_manifest(file_path):
    """Load the dataset manifest."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Manifest not found: {file_path}"
        )

    return pd.read_csv(file_path)


def split_dataset(
    manifest,
    train_ratio=0.70,
    validation_ratio=0.15,
    test_ratio=0.15,
    random_state=42,
):
    """Split the dataset into train, validation, and test sets."""

    total_ratio = train_ratio + validation_ratio + test_ratio

    if abs(total_ratio - 1.0) > 1e-6:
        raise ValueError(
            "Train, validation, and test ratios must add up to 1.0."
        )

    if "patient_id" not in manifest.columns:
        raise ValueError(
            "Manifest must contain a 'patient_id' column "
            "for patient-level splitting."
        )

    unique_patients = manifest["patient_id"].dropna().unique()

    if len(unique_patients) < 3:
        raise ValueError(
            "At least 3 unique patients are required for splitting."
        )

    train_patients, temporary_patients = train_test_split(
        unique_patients,
        test_size=(validation_ratio + test_ratio),
        random_state=random_state,
    )

    validation_fraction = (
        validation_ratio /
        (validation_ratio + test_ratio)
    )

    validation_patients, test_patients = train_test_split(
        temporary_patients,
        test_size=(1 - validation_fraction),
        random_state=random_state,
    )

    train_set = manifest[
        manifest["patient_id"].isin(train_patients)
    ].copy()

    validation_set = manifest[
        manifest["patient_id"].isin(validation_patients)
    ].copy()

    test_set = manifest[
        manifest["patient_id"].isin(test_patients)
    ].copy()

    return train_set, validation_set, test_set


def save_splits(
    train_set,
    validation_set,
    test_set,
    output_directory,
):
    """Save dataset splits as CSV files."""

    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    train_set.to_csv(
        output_directory / "train.csv",
        index=False,
    )

    validation_set.to_csv(
        output_directory / "validation.csv",
        index=False,
    )

    test_set.to_csv(
        output_directory / "test.csv",
        index=False,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Create patient-level train, validation, and test splits."
    )

    parser.add_argument(
        "manifest",
        help="Path to the dataset manifest CSV",
    )

    parser.add_argument(
        "--output",
        default="03_Dataset/splits",
        help="Directory for split files",
    )

    args = parser.parse_args()

    try:
        manifest = load_manifest(args.manifest)

        train_set, validation_set, test_set = split_dataset(
            manifest
        )

        save_splits(
            train_set,
            validation_set,
            test_set,
            args.output,
        )

        print("\n=== PediVision Dataset Split ===")
        print(f"Total records: {len(manifest)}")
        print(f"Training records: {len(train_set)}")
        print(f"Validation records: {len(validation_set)}")
        print(f"Test records: {len(test_set)}")

        print("\nUnique patients:")
        print(f"Training: {train_set['patient_id'].nunique()}")
        print(f"Validation: {validation_set['patient_id'].nunique()}")
        print(f"Test: {test_set['patient_id'].nunique()}")

        print("\nDataset splitting completed successfully.")

    except Exception as error:
        print(f"\nError splitting dataset: {error}")


if __name__ == "__main__":
    main()