from pathlib import Path
import argparse

import pandas as pd


def find_mri_files(data_directory):
    """Find all supported NIfTI MRI files recursively."""

    data_directory = Path(data_directory)

    if not data_directory.exists():
        raise FileNotFoundError(
            f"Data directory not found: {data_directory}"
        )

    mri_files = []

    for file_path in data_directory.rglob("*"):
        if not file_path.is_file():
            continue

        name = file_path.name.lower()

        if name.endswith(".nii") or name.endswith(".nii.gz"):
            mri_files.append(file_path)

    return sorted(mri_files)


def build_manifest(data_directory, output_file):
    """Create a basic MRI file manifest."""

    mri_files = find_mri_files(data_directory)

    records = []

    for file_path in mri_files:
        records.append(
            {
                "file_name": file_path.name,
                "file_path": str(file_path),
                "file_extension": (
                    ".nii.gz"
                    if file_path.name.lower().endswith(".nii.gz")
                    else ".nii"
                ),
            }
        )

    manifest = pd.DataFrame(
        records,
        columns=[
            "file_name",
            "file_path",
            "file_extension",
        ],
    )

    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    manifest.to_csv(output_file, index=False)

    print("\n=== PediVision Dataset Manifest ===")
    print(f"Data directory: {data_directory}")
    print(f"MRI files found: {len(mri_files)}")
    print(f"Manifest saved to: {output_file}")

    if len(mri_files) == 0:
        print("\nNo MRI files found.")
        print("This is expected until the approved dataset is available.")

    print("\nManifest creation completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Build a manifest of PediVision MRI files."
    )

    parser.add_argument(
        "data_directory",
        help="Directory containing MRI files",
    )

    parser.add_argument(
        "--output",
        default="03_Dataset/mri_manifest.csv",
        help="Output CSV path",
    )

    args = parser.parse_args()

    try:
        build_manifest(
            args.data_directory,
            args.output,
        )

    except Exception as error:
        print(f"\nError creating manifest: {error}")


if __name__ == "__main__":
    main()