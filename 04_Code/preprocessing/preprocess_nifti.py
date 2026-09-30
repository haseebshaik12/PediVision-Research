from pathlib import Path
import argparse

import nibabel as nib
import numpy as np


def load_nifti(file_path):
    """Load a NIfTI MRI file and return the image data."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    image = nib.load(str(file_path))
    data = image.get_fdata(dtype=np.float32)

    return image, data


def normalize_intensity(data):
    """Normalize MRI intensity values to the range 0-1."""

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


def preprocess_nifti(file_path):
    """Load and normalize a NIfTI MRI file."""

    image, data = load_nifti(file_path)

    print("\n=== PediVision MRI Preprocessing ===")
    print(f"File: {Path(file_path).name}")
    print(f"Original dimensions: {data.shape}")

    normalized_data = normalize_intensity(data)

    print("\n=== Normalization ===")
    print(f"Normalized minimum: {normalized_data.min():.4f}")
    print(f"Normalized maximum: {normalized_data.max():.4f}")
    print(f"Normalized mean: {normalized_data.mean():.4f}")

    print("\nPreprocessing completed successfully.")

    return image, normalized_data


def main():
    parser = argparse.ArgumentParser(
        description="Preprocess a NIfTI MRI file for PediVision."
    )

    parser.add_argument(
        "file_path",
        help="Path to the NIfTI MRI file (.nii or .nii.gz)"
    )

    args = parser.parse_args()

    try:
        preprocess_nifti(args.file_path)

    except Exception as error:
        print(f"\nError during preprocessing: {error}")


if __name__ == "__main__":
    main()