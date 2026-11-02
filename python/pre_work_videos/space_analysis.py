"""Space Complexity Assignment: classifications and duplicate email detection.

Both CSV approaches assume a column named 'email'.
Run: python space_complexity_assignment.py emails.csv
"""

import csv
import sys
# The list holds all n emails; Python's list.sort() can need O(n)
# additional temporary memory in the worst case.
def duplicates_with_sort(csv_path):
    emails = []
    with open(csv_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "email" not in reader.fieldnames:
            raise ValueError("CSV must have an 'email' column")
        for row in reader:
            email = (row["email"] or "").strip()
            if email:
                emails.append(email)

    emails.sort()
    duplicates = []
    for i in range(1, len(emails)):
        if emails[i] == emails[i - 1]:
            # Only record each duplicated address once.
            if not duplicates or duplicates[-1] != emails[i]:
                duplicates.append(emails[i])
    return duplicates


def duplicates_with_set(csv_path):
    seen = set()
    duplicates = set()

    with open(csv_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or "email" not in reader.fieldnames:
            raise ValueError("CSV must have an 'email' column")
        for row in reader:
            email = (row["email"] or "").strip()
            if not email:
                continue
            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates


# RAM tradeoff:
# 4 GB: Prefer sort-and-scan when memory is the priority; a list generally
# uses less memory per email than a set. With 5 million rows, measure actual
# usage first: both O(n) methods may still exceed available RAM.
# 64 GB: Prefer the set approach for its O(n) expected processing time,
# trading extra memory for speed.


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python space_complexity_assignment.py emails.csv")
        sys.exit(1)

    path = sys.argv[1]
    try:
        set_result = duplicates_with_set(path)
        sort_result = duplicates_with_sort(path)
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    print("Duplicates (set):", sorted(set_result))
    print("Duplicates (sort and scan):", sort_result)
    assert set_result == set(sort_result), "Approaches returned different results"