"""
PediVision AI
Dataset Intake and Verification

Purpose:
    Perform an initial structural inspection of the approved research dataset
    before any preprocessing or model training.

Important:
    This script does not modify patient data.
    It does not assume specific CBTN variables, MRI sequences, or labels.
    Dataset-specific fields must be verified after access is granted.
"""

from pathlib import Path
import csv


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = PROJECT_ROOT / "data" / "raw"


# File types that may be encountered in an imaging dataset.
MRI_EXTENSIONS = {
    ".nii",
    ".nii.gz",
    ".dcm",
    ".dicom",
}

TABULAR_EXTENSIONS = {
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
}


def get_files_by_type(root: Path):
    """Collect files under the dataset directory by broad file type."""

    results = {
        "mri": [],
        "tabular": [],
        "other": [],
    }

    if not root.exists():
        return results

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        name = path.name.lower()

        if name.endswith(".nii.gz"):
            results["mri"].append(path)
            continue

        suffix = path.suffix.lower()

        if suffix in {".nii", ".dcm", ".dicom"}:
            results["mri"].append(path)
        elif suffix in TABULAR_EXTENSIONS:
            results["tabular"].append(path)
        else:
            results["other"].append(path)

    return results


def inspect_csv(path: Path):
    """Perform a lightweight inspection of a CSV file."""

    print(f"\nCSV file: {path.relative_to(PROJECT_ROOT)}")

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)

            header = next(reader, None)

            if header is None:
                print("  Status: empty file")
                return

            rows = sum(1 for _ in reader)

        print(f"  Columns: {len(header)}")
        print(f"  Rows: {rows}")
        print(f"  Column names: {header}")

    except Exception as exc:
        print(f"  Could not inspect CSV: {exc}")


def main():
    print("=" * 70)
    print("PediVision AI — Dataset Intake and Verification")
    print("=" * 70)

    print(f"\nDataset directory:")
    print(DATA_RAW)

    if not DATA_RAW.exists():
        print("\nSTATUS: data/raw does not exist.")
        print("Create the directory before placing approved research data.")
        return

    results = get_files_by_type(DATA_RAW)

    print("\nFile summary")
    print("-" * 70)
    print(f"MRI/image files : {len(results['mri'])}")
    print(f"Tabular files   : {len(results['tabular'])}")
    print(f"Other files     : {len(results['other'])}")

    if results["mri"]:
        print("\nMRI/image files:")
        for path in results["mri"][:20]:
            print(f"  - {path.relative_to(DATA_RAW)}")

        if len(results["mri"]) > 20:
            print(f"  ... and {len(results['mri']) - 20} more")

    if results["tabular"]:
        print("\nTabular files:")
        for path in results["tabular"]:
            print(f"  - {path.relative_to(DATA_RAW)}")

            if path.suffix.lower() == ".csv":
                inspect_csv(path)

    if results["other"]:
        print("\nOther files:")
        for path in results["other"][:20]:
            print(f"  - {path.relative_to(DATA_RAW)}")

        if len(results["other"]) > 20:
            print(f"  ... and {len(results['other']) - 20} more")

    print("\n" + "=" * 70)
    print("Dataset-specific verification is required before model training.")
    print("Do not assume labels, MRI sequences, patient IDs, or clinical fields.")
    print("=" * 70)


if __name__ == "__main__":
    main()