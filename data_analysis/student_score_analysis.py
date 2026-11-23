"""Student Score Analysis -pandas assignment."""

import pandas as pd

# Step 1: Create a DataFrame from the provided student information.
data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}

df = pd.DataFrame(data)

# Question 1: Count the number of students in each course.
print("1. Number of students in each course:")
print(df["course"].value_counts().sort_index())
print()

# Question 2: Find the average score for each course.
print("2. Average score per course:")
print(df.groupby("course")["score"].mean().round(2))
print()

# Question 3: Display the three students with the highest scores.
print("3. Top 3 students by score:")
print(df.nlargest(3, "score")[["student", "course", "score"]].to_string(index=False))
print()

# Question 4: Compare the average hours studied for passed and failed students.
print("4. Average hours studied by pass status:")
print(df.groupby("passed")["hours_studied"].mean().rename(index={True: "Passed", False: "Did not pass"}).round(2))
print()

# Question 5: Create grades using score ranges (no loops needed).
# pd.cut places each score into the matching grade category.
df["grade"] = pd.cut(
    df["score"],
    bins=[-float("inf"), 69, 79, 89, float("inf")],
    labels=["F", "C", "B", "A"],
).astype(str)

print("5. Students with their grades:")
print(df[["student", "course", "score", "grade"]].to_string(index=False))
print()

# Question 6: Count each grade in each course.
# Unstack displays the grades as separate columns.
print("6. Grade distribution per course:")
grade_distribution = pd.crosstab(df["course"], df["grade"])
print(grade_distribution.reindex(columns=["A", "B", "C", "F"], fill_value=0))
