"""Clean, analyze, and chart employee survey data."""

from datetime import datetime
from pathlib import Path
import warnings

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import pandas as pd


COLUMNS = (
    "employee_id", "name", "department", "office_location", "salary",
    "years_experience", "satisfaction_score", "survey_date", "comments",
)
DEPARTMENTS = {"eng": "Engineering", "hr": "Human Resources"}
OFFICES = {"nyc": "New York"}
DATE_FORMATS = ("%Y-%m-%d", "%m/%d/%Y", "%m-%d-%Y", "%b %d, %Y", "%B %d, %Y")


def parse_date(value):
    """Try the supported formats, using month-first for numeric US dates."""
    if not value:
        return pd.NaT
    for date_format in DATE_FORMATS:
        try:
            return datetime.strptime(value, date_format)
        except ValueError:
            continue
    return pd.NaT


class DataPipeline:
    """A reusable data processing pipeline for employee surveys."""

    def __init__(self, filepath):
        """Load the input as text so IDs and messy values can be cleaned."""
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error", pd.errors.ParserWarning)
                raw = pd.read_csv(filepath, dtype=str, keep_default_na=False,
                                  encoding="utf-8-sig", index_col=False,
                                  on_bad_lines="error")
        except (OSError, UnicodeError, pd.errors.ParserError,
                pd.errors.ParserWarning, pd.errors.EmptyDataError) as error:
            raise ValueError(f"Could not read CSV {filepath}: {error}") from error

        raw.columns = raw.columns.str.strip().str.lower()
        missing = [column for column in COLUMNS if column not in raw]
        if missing:
            raise ValueError(f"Missing required CSV columns: {', '.join(missing)}")
        self.raw_data = raw.loc[:, list(COLUMNS)]
        self.data = None

    def clean(self):
        """Clean a fresh copy of the raw data and return self for chaining."""
        data = self.raw_data.copy()
        for column in COLUMNS:
            data[column] = data[column].fillna("").str.strip()

        data["employee_id"] = data["employee_id"].str.upper()
        has_id = data["employee_id"].ne("")
        missing_ids = int((~has_id).sum())
        data = data.loc[has_id].copy()
        duplicate_ids = data["employee_id"].duplicated(keep="first")
        duplicates = int(duplicate_ids.sum())
        data = data.loc[~duplicate_ids].reset_index(drop=True)

        filled = 0
        for column in ("name", "department", "office_location"):
            values = data[column].str.replace(r"\s+", " ", regex=True)
            filled += int(values.eq("").sum())
            data[column] = values.str.title().replace("", "Unknown")

        for column, aliases in (("department", DEPARTMENTS),
                                ("office_location", OFFICES)):
            alternate = data[column].str.lower().map(aliases)
            data[column] = alternate.fillna(data[column])

        quality = {}
        for column, minimum, maximum in (
            ("salary", 0, float("inf")),
            ("years_experience", 0, 50),
            ("satisfaction_score", 1, 10),
        ):
            original = data[column]
            values = original
            if column == "salary":
                currency = values.str.fullmatch(
                    r"[+-]?\$?(?:\d+|\d{1,3}(?:,\d{3})+)(?:\.\d+)?"
                )
                values = values.where(currency).str.replace(r"[$,]", "", regex=True)
            numbers = pd.to_numeric(values, errors="coerce")
            valid = numbers.between(minimum, maximum) & numbers.ne(float("inf"))
            data[column] = numbers.where(valid).astype("Float64")
            quality[column] = (int(original.eq("").sum()),
                               int((original.ne("") & ~valid).sum()))

        original_dates = data["survey_date"]
        data["survey_date"] = pd.to_datetime(original_dates.map(parse_date), errors="coerce")
        quality["survey_date"] = (
            int(original_dates.eq("").sum()),
            int((original_dates.ne("") & data["survey_date"].isna()).sum()),
        )
        self.data = data

        print(f"Cleaning summary: removed {duplicates} duplicates and {missing_ids} "
              f"rows without an ID. Filled {filled} blank text values with Unknown. "
              f"Kept {len(data)} of {len(self.raw_data)} rows.")
        for column, (missing, invalid) in quality.items():
            print(f"  {column}: {missing} missing, {invalid} invalid. Exported as blanks.")
        print(f"  comments: {int(data['comments'].eq('').sum())} blank after trimming.")
        return self

    def analyze(self):
        """Calculate grouped statistics using valid responses."""
        data = self._cleaned_data()
        departments = data.groupby("department")
        paired = data[["years_experience", "salary"]].dropna()
        correlation = None
        if len(paired) >= 2 and paired.nunique().gt(1).all():
            correlation = round(float(paired["years_experience"].corr(paired["salary"])), 4)

        scores = data["satisfaction_score"].dropna()
        return {
            "Average salary by department": self._means(departments["salary"]),
            "Average satisfaction by department": self._means(departments["satisfaction_score"]),
            "Headcount by office": data["office_location"].value_counts().sort_index().to_dict(),
            "Experience vs. salary (Pearson r)": correlation,
            "Responses used for correlation": len(paired),
            "Percent of valid ratings at 8–10": round(float(scores.ge(8).mean()) * 100, 1)
            if len(scores) else None,
            "Valid satisfaction responses": len(scores),
        }

    @staticmethod
    def _means(grouped):
        return {group: round(float(mean), 2) if pd.notna(mean) else None
                for group, mean in grouped.mean().items()}

    def _cleaned_data(self):
        if self.data is None:
            raise ValueError("Call clean() before analyzing, charting, or exporting.")
        return self.data

    def visualize(self, output_path="output/charts.png"):
        """Save a department salary bar chart and satisfaction histogram."""
        data = self._cleaned_data()
        salaries = data.groupby("department")["salary"].mean().dropna().sort_values()
        scores = data["satisfaction_score"].dropna()
        fig, (salary_ax, score_ax) = plt.subplots(1, 2, figsize=(12, 4.5),
                                                 layout="constrained")
        try:
            if len(salaries):
                salary_ax.barh(salaries.index, salaries.astype(float), color="#176B67")
            else:
                salary_ax.text(.5, .5, "No valid salaries", ha="center",
                               transform=salary_ax.transAxes)
            salary_ax.set(title="Average salary by department", xlabel="Annual salary (USD)")
            salary_ax.xaxis.set_major_formatter(StrMethodFormatter("${x:,.0f}"))
            salary_ax.tick_params(axis="x", labelrotation=25)

            score_ax.hist(scores.astype(float), bins=[x - .5 for x in range(1, 12)],
                          color="#345DA7", edgecolor="white")
            if scores.empty:
                score_ax.text(.5, .5, "No valid ratings", ha="center",
                              transform=score_ax.transAxes)
            score_ax.set(title=f"Satisfaction distribution (n={len(scores)})",
                         xlabel="Satisfaction rating (1–10)", ylabel="Responses",
                         xticks=range(1, 11))
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(path, dpi=160)
        except (OSError, ValueError) as error:
            raise ValueError(f"Could not save chart {output_path}: {error}") from error
        finally:
            plt.close(fig)

    def export(self, output_path="output/clean_data.csv"):
        """Export cleaned data with ISO dates and blank missing values."""
        data = self._cleaned_data()
        try:
            path = Path(output_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            data.to_csv(path, index=False, date_format="%Y-%m-%d")
        except (OSError, ValueError) as error:
            raise ValueError(f"Could not export CSV {output_path}: {error}") from error

    def run(self):
        """Run the complete pipeline and return its analysis summary."""
        self.clean()
        results = self.analyze()
        self.visualize()
        self.export()
        return results
