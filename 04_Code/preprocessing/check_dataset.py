
from pathlib import Path
from collections import Counter
import argparse


def inspect_dataset(dataset_path):
    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        print(f"Error: Folder not found: {dataset_path}")
        return

    if not dataset_path.is_dir():
        print("Error: The provided path is not a folder.")
        return

    print("\n=== PediVision Dataset Inspection ===")
    print(f"Dataset folder: {dataset_path.resolve()}")

    file_count = 0
    folder_count = 0
    extensions = Counter()

    print("\n=== Folder Structure ===")

    for item in sorted(dataset_path.rglob("*")):
        relative_path = item.relative_to(dataset_path)

        if item.is_dir():
            folder_count += 1
            print(f"[FOLDER] {relative_path}")
        elif item.is_file():
            file_count += 1
            extension = item.suffix.lower() or "No extension"
            extensions[extension] += 1
            print(f"[FILE]   {relative_path}")

    print("\n=== Summary ===")
    print(f"Total folders: {folder_count}")
    print(f"Total files: {file_count}")

    print("\n=== File Types ===")

    if extensions:
        for extension, count in sorted(extensions.items()):
            print(f"{extension}: {count} files")
    else:
        print("No files found.")

    print("\nInspection completed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Inspect the folder structure of a dataset."
    )
    parser.add_argument(
        "dataset_path",
        help="Path to the dataset folder"
    )
    args = parser.parse_args()

    inspect_dataset(args.dataset_path)