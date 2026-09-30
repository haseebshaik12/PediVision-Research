from pathlib import Path
import argparse

import numpy as np
import nibabel as nib


def load_mri(file_path):
    """Load a NIfTI MRI file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"MRI file not found: {file_path}")

    image = nib.load(str(file_path))
    data = image.get_fdata(dtype=np.float32)

    return image, data


def normalize_mri(data):
    """Normalize finite MRI intensity values to the range 0-1."""

    finite_mask = np.isfinite(data)

    if not np.any(finite_mask):
        raise ValueError("MRI contains no valid numerical values.")

    valid_data = data[finite_mask]

    minimum = valid_data.min()
    maximum = valid_data.max()

    if maximum == minimum:
        return np.zeros_like(data, dtype=np.float32)

    normalized = (data - minimum) / (maximum - minimum)

    normalized[~finite_mask] = 0

    return normalized.astype(np.float32)


def prepare_mri(file_path):
    """Load and normalize one MRI file."""

    image, data = load_mri(file_path)

    normalized_data = normalize_mri(data)

    print("\n=== PediVision MRI Training Preparation ===")
    print(f"File: {Path(file_path).name}")
    print(f"Original shape: {data.shape}")
    print(f"Normalized shape: {normalized_data.shape}")
    print(f"Minimum intensity: {normalized_data.min():.4f}")
    print(f"Maximum intensity: {normalized_data.max():.4f}")

    print("\nMRI preparation completed successfully.")

    return image, normalized_data


def main():
    parser = argparse.ArgumentParser(
        description="Prepare MRI data for PediVision model training."
    )

    parser.add_argument(
        "file_path",
        help="Path to a NIfTI MRI file (.nii or .nii.gz)"
    )

    args = parser.parse_args()

    try:
        prepare_mri(args.file_path)

    except Exception as error:
        print(f"\nError preparing MRI: {error}")


if __name__ == "__main__":
    main()