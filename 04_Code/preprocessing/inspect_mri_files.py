
from pathlib import Path
from collections import Counter
import argparse


def inspect_mri_files(dataset_path):
    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        print(f"Error: Folder not found: {dataset_path}")
        return

    if not dataset_path.is_dir():
        print("Error: The provided path is not a folder.")
        return

    print("\n=== PediVision MRI File Inspection ===")
    print(f"Dataset folder: {dataset_path.resolve()}")

    extensions = Counter()
    total_files = 0

    for file_path in sorted(dataset_path.rglob("*")):
        if not file_path.is_file():
            continue

        total_files += 1
        name = file_path.name.lower()

        if name.endswith(".nii.gz"):
            extension = ".nii.gz"
        else:
            extension = file_path.suffix.lower() or "No extension"

        extensions[extension] += 1

    print("\n=== File Format Summary ===")
    print(f"Total files: {total_files}")

    if extensions:
        for extension, count in sorted(extensions.items()):
            print(f"{extension}: {count} files")
    else:
        print("No files found.")

    print("\n=== MRI Format Guidance ===")

    mri_formats = {".nii", ".nii.gz", ".dcm"}

    found_mri = any(
        extension in mri_formats for extension in extensions
    )

    if found_mri:
        print("Potential MRI file formats detected.")
        print("File extensions alone cannot confirm valid MRI data.")
    else:
        print("No common MRI file extensions detected.")

    print("\nInspection completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inspect MRI file formats in a dataset folder."
    )
    parser.add_argument(
        "dataset_path",
        help="Path to the dataset folder"
    )
    args = parser.parse_args()

    inspect_mri_files(args.dataset_path)