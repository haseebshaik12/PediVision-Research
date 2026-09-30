from pathlib import Path
import argparse

import pandas as pd


def load_clinical_data(file_path):
    """Load a clinical CSV file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Clinical data file not found: {file_path}"
        )

    if file_path.suffix.lower() != ".csv":
        raise ValueError("Clinical data must be a CSV file.")

    return pd.read_csv(file_path)


def inspect_multimodal_data(mri_manifest_path, clinical_data_path):
    """Inspect MRI and clinical data before multimodal modeling."""

    mri_manifest_path = Path(mri_manifest_path)

    if not mri_manifest_path.exists():
        raise FileNotFoundError(
            f"MRI manifest not found: {mri_manifest_path}"
        )

    mri_manifest = pd.read_csv(mri_manifest_path)
    clinical_data = load_clinical_data(clinical_data_path)

    print("\n=== PediVision Multimodal Dataset ===")

    print("\nMRI Manifest")
    print(f"MRI records: {len(mri_manifest)}")
    print(f"MRI columns: {list(mri_manifest.columns)}")

    print("\nClinical Data")
    print(f"Clinical records: {len(clinical_data)}")
    print(f"Clinical columns: {list(clinical_data.columns)}")

    print("\nImportant:")
    print("MRI and clinical records must be matched using an appropriate")
    print("de-identified study/patient identifier from the approved dataset.")

    print("\nMultimodal dataset inspection completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Inspect MRI and clinical data for multimodal modeling."
    )

    parser.add_argument(
        "mri_manifest",
        help="Path to the MRI manifest CSV",
    )

    parser.add_argument(
        "clinical_data",
        help="Path to the clinical CSV",
    )

    args = parser.parse_args()

    try:
        inspect_multimodal_data(
            args.mri_manifest,
            args.clinical_data,
        )

    except Exception as error:
        print(f"\nError inspecting multimodal data: {error}")


if __name__ == "__main__":
    main()