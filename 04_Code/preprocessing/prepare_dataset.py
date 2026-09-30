from pathlib import Path
import argparse


MRI_EXTENSIONS = {".nii", ".nii.gz"}


def is_mri_file(file_path):
    """Check whether a file has a supported MRI file extension."""

    name = file_path.name.lower()

    return (
        name.endswith(".nii")
        or name.endswith(".nii.gz")
    )


def find_mri_files(input_directory):
    """Find all NIfTI MRI files inside a directory recursively."""

    input_directory = Path(input_directory)

    if not input_directory.exists():
        raise FileNotFoundError(
            f"Input directory not found: {input_directory}"
        )

    mri_files = [
        file_path
        for file_path in input_directory.rglob("*")
        if file_path.is_file() and is_mri_file(file_path)
    ]

    return sorted(mri_files)


def inspect_dataset(input_directory):
    """Inspect an MRI dataset directory."""

    mri_files = find_mri_files(input_directory)

    print("\n=== PediVision Dataset Preparation ===")
    print(f"Dataset directory: {input_directory}")
    print(f"Total MRI files found: {len(mri_files)}")

    if not mri_files:
        print("\nNo NIfTI MRI files were found.")
        print("This is expected if the dataset has not been downloaded yet.")
        return

    print("\nFirst MRI files found:")

    for file_path in mri_files[:10]:
        print(f"- {file_path}")

    if len(mri_files) > 10:
        print(f"\n... and {len(mri_files) - 10} more files.")

    print("\nDataset inspection completed.")


def main():
    parser = argparse.ArgumentParser(
        description="Inspect and prepare a PediVision MRI dataset."
    )

    parser.add_argument(
        "input_directory",
        help="Directory containing MRI files"
    )

    args = parser.parse_args()

    try:
        inspect_dataset(args.input_directory)

    except Exception as error:
        print(f"\nError preparing dataset: {error}")


if __name__ == "__main__":
    main()