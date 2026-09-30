from pathlib import Path
import argparse

import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt


def visualize_nifti(file_path):
    """Display the central axial, coronal, and sagittal MRI slices."""

    file_path = Path(file_path)

    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return

    try:
        image = nib.load(str(file_path))
        data = image.get_fdata(dtype=np.float32)

        if data.ndim != 3:
            print(f"Error: Expected a 3D MRI image, got {data.ndim}D.")
            return

        # Select the middle slice in each orientation
        x, y, z = [dim // 2 for dim in data.shape]

        axial = data[:, :, z]
        coronal = data[:, y, :]
        sagittal = data[x, :, :]

        # Display the slices
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        axes[0].imshow(
            np.rot90(axial), cmap="gray", origin="lower"
        )
        axes[0].set_title("Axial")

        axes[1].imshow(
            np.rot90(coronal), cmap="gray", origin="lower"
        )
        axes[1].set_title("Coronal")

        axes[2].imshow(
            np.rot90(sagittal), cmap="gray", origin="lower"
        )
        axes[2].set_title("Sagittal")

        for ax in axes:
            ax.axis("off")

        fig.suptitle(f"MRI Visualization: {file_path.name}")
        plt.tight_layout()
        plt.show()

    except Exception as error:
        print(f"Error visualizing MRI: {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Visualize the central slices of a 3D NIfTI MRI."
    )
    parser.add_argument(
        "file_path",
        help="Path to a NIfTI file (.nii or .nii.gz)"
    )

    args = parser.parse_args()
    visualize_nifti(args.file_path)


if __name__ == "__main__":
    main()