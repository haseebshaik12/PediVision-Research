from pathlib import Path
import argparse

import nibabel as nib
import numpy as np
import pandas as pd


def load_mri(file_path):
    """Load a NIfTI MRI file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"MRI file not found: {file_path}"
        )

    image = nib.load(str(file_path))
    data = image.get_fdata(dtype=np.float32)

    return data


def normalize_mri(data):
    """Normalize finite MRI intensities to 0-1."""

    finite_mask = np.isfinite(data)

    if not np.any(finite_mask):
        raise ValueError(
            "MRI contains no valid numerical values."
        )

    valid_data = data[finite_mask]

    minimum = valid_data.min()
    maximum = valid_data.max()

    if maximum == minimum:
        return np.zeros_like(data, dtype=np.float32)

    normalized = (data - minimum) / (maximum - minimum)
    normalized[~finite_mask] = 0

    return normalized.astype(np.float32)


def extract_features(data):
    """Extract basic numerical MRI features."""

    finite_data = data[np.isfinite(data)]

    features = {
        "mean_intensity": float(np.mean(finite_data)),
        "std_intensity": float(np.std(finite_data)),
        "minimum_intensity": float(np.min(finite_data)),
        "maximum_intensity": float(np.max(finite_data)),
        "median_intensity": float(np.median(finite_data)),
    }

    return features


def main():
    parser = argparse.ArgumentParser(
        description="Extract basic numerical features from an MRI."
    )

    parser.add_argument(
        "file_path",
        help="Path to a NIfTI MRI file",
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Optional output CSV path",
    )

    args = parser.parse_args()

    try:
        data = load_mri(args.file_path)
        normalized_data = normalize_mri(data)
        features = extract_features(normalized_data)

        print("\n=== PediVision MRI Feature Extraction ===")
        print(f"File: {Path(args.file_path).name}")
        print(f"MRI shape: {data.shape}")

        print("\n=== Extracted Features ===")

        for name, value in features.items():
            print(f"- {name}: {value:.6f}")

        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            pd.DataFrame([features]).to_csv(
                output_path,
                index=False,
            )

            print(f"\nFeatures saved to: {output_path}")

        print("\nMRI feature extraction completed.")

    except Exception as error:
        print(f"\nError extracting MRI features: {error}")


if __name__ == "__main__":
    main()