"""Run the employee survey pipeline from the command line."""

import argparse
import sys

from pipeline import DataPipeline


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv", nargs="?", default="data/messy_employee_survey.csv")
    args = parser.parse_args()

    try:
        results = DataPipeline(args.csv).run()
    except ValueError as error:
        print(f"Pipeline error: {error}", file=sys.stderr)
        return 1

    print("\n=== Analysis Results ===")
    for key, value in results.items():
        print(f"{key}: {value}")
    print("\nSaved output/clean_data.csv and output/charts.png.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
