from pathlib import Path
import argparse

import pandas as pd


def load_csv(file_path):
    """Load a CSV file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    return pd.read_csv(file_path)


def combine_features(
    mri_features_path,
    clinical_features_path,
    output_path,
):
    """Combine MRI and clinical features using a shared patient ID."""

    mri_data = load_csv(mri_features_path)
    clinical_data = load_csv(clinical_features_path)

    if "patient_id" not in mri_data.columns:
        raise ValueError(
            "MRI feature data must contain 'patient_id'."
        )

    if "patient_id" not in clinical_data.columns:
        raise ValueError(
            "Clinical feature data must contain 'patient_id'."
        )

    combined_data = pd.merge(
        mri_data,
        clinical_data,
        on="patient_id",
        how="inner",
        suffixes=("_mri", "_clinical"),
    )

    output_path = Path(output_path)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    combined_data.to_csv(
        output_path,
        index=False,
    )

    print("\n=== PediVision Multimodal Feature Combination ===")
    print(f"MRI records: {len(mri_data)}")
    print(f"Clinical records: {len(clinical_data)}")
    print(f"Matched records: {len(combined_data)}")
    print(f"Combined features: {len(combined_data.columns)}")
    print(f"Output: {output_path}")

    print("\nMultimodal feature combination completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Combine MRI and clinical features."
    )

    parser.add_argument(
        "mri_features",
        help="MRI feature CSV",
    )

    parser.add_argument(
        "clinical_features",
        help="Clinical feature CSV",
    )

    parser.add_argument(
        "--output",
        default="03_Dataset/multimodal_features.csv",
        help="Output CSV path",
    )

    args = parser.parse_args()

    try:
        combine_features(
            args.mri_features,
            args.clinical_features,
            args.output,
        )

    except Exception as error:
        print(f"\nError combining features: {error}")


if __name__ == "__main__":
    main()
    