from pathlib import Path
import argparse

import pandas as pd


def load_results(file_path):
    """Load experiment results."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Results file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def compare_experiments(results):
    """Display experiment results for comparison."""

    required_columns = {
        "experiment",
        "accuracy",
    }

    missing_columns = required_columns - set(results.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    print("\n=== PediVision Experiment Comparison ===")

    print(
        results[
            ["experiment", "accuracy"]
        ].to_string(index=False)
    )

    print(
        "\nImportant: Results must come from the "
        "same evaluation protocol and test set."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Compare PediVision experiment results."
    )

    parser.add_argument(
        "results_file",
        help="CSV containing experiment results",
    )

    args = parser.parse_args()

    try:
        results = load_results(args.results_file)
        compare_experiments(results)

        print("\nExperiment comparison completed.")

    except Exception as error:
        print(
            f"\nError comparing experiments: {error}"
        )


if __name__ == "__main__":
    main()