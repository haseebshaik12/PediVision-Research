from pathlib import Path
import argparse

import nibabel as nib
import numpy as np


def inspect_nifti(file_path):
    """Inspect a NIfTI MRI file and report its basic properties."""

    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return

    try:
        # Load the MRI image
        image = nib.load(str(file_path))

        # Get image information
        shape = image.shape
        spacing = image.header.get_zooms()
        dtype = image.get_data_dtype()

        print("\n=== PediVision NIfTI Inspection ===")
        print(f"File: {file_path.name}")
        print(f"Image dimensions: {shape}")
        print(f"Number of dimensions: {len(shape)}")
        print(f"Voxel spacing (mm): {spacing}")
        print(f"Image data type: {dtype}")

        # Load image data for numerical inspection
        data = image.get_fdata(dtype=np.float32)

        # Check for valid numerical values
        finite_mask = np.isfinite(data)
        finite_count = int(np.count_nonzero(finite_mask))
        total_count = int(data.size)

        print("\n=== Numerical Data Check ===")
        print(f"Total voxels/values: {total_count}")
        print(f"Finite values: {finite_count}")
        print(f"Non-finite values: {total_count - finite_count}")

        if finite_count > 0:
            finite_data = data[finite_mask]
            print(f"Minimum intensity: {finite_data.min():.4f}")
            print(f"Maximum intensity: {finite_data.max():.4f}")
            print(f"Mean intensity: {finite_data.mean():.4f}")
            print(f"Contains valid numerical values: Yes")
        else:
            print("Contains valid numerical values: No")

        print("\nInspection completed.")

    except Exception as error:
        print(f"Error inspecting NIfTI file: {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a NIfTI MRI file."
    )
    parser.add_argument(
        "file_path",
        help="Path to the NIfTI file (.nii or .nii.gz)"
    )

    args = parser.parse_args()
    inspect_nifti(args.file_path)


if __name__ == "__main__":
    main()