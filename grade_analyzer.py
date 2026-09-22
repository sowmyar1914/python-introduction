# starting with the list of grades, we will calculate the average, highest, and lowest grades.
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# variables to count each letter grade
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

# variables to know the passing and failing students
passing_count = 0
failing_count = 0

# evaluating each score in the list to determine letter grades
# and passing/failing counts
for score in scores:

    if score >= 90:
        a_count += 1
        passing_count += 1

    elif score >= 80:
        b_count += 1
        passing_count += 1

    elif score >= 70:
        c_count += 1
        passing_count += 1

    elif score >= 60:
        d_count += 1
        passing_count += 1

    else:
        f_count += 1
        failing_count += 1


# calculating the average, highest, and lowest grades
TOTAL_SCORES = len(scores)

AVERAGE_SCORE = sum(scores) / TOTAL_SCORES

HIGHEST_SCORE = max(scores)

LOWEST_SCORE = min(scores)


# calculating percentages
passing_percentage = (passing_count / TOTAL_SCORES) * 100
failing_percentage = (failing_count / TOTAL_SCORES) * 100


# displaying the results
print("=== Grade Analyzer ===")

print(f"Total scores: {TOTAL_SCORES}")

print(f"Average: {AVERAGE_SCORE:.1f}")

print(f"Highest: {HIGHEST_SCORE}")

print(f"Lowest: {LOWEST_SCORE}")

print(
    f"Passing: {passing_count} "
    f"({passing_percentage:.1f}%)"
)

print(
    f"Failing: {failing_count} "
    f"({failing_percentage:.1f}%)"
)


print("\nGrade Distribution:")

print(f"A: {a_count} students")

print(f"B: {b_count} students")

print(f"C: {c_count} students")

print(f"D: {d_count} students")

print(f"F: {f_count} students")


# while loop to allow the user to input additional scores
print("\n--- Add More Scores ---")

while True:

    user_input = input(
        "Enter a score (or 'done' to finish): "
    )

    # stop the loop when the user types done
    if user_input.lower() == "done":
        break

    # convert user input into a number
    new_score = float(user_input)

    # add the new score to the scores list
    scores.append(new_score)

    # calculate the updated average
    updated_average_score = sum(scores) / len(scores)

    print(
        f"Updated average: "
        f"{updated_average_score:.1f}"
    )


# final average score after adding new scores
final_average_score = sum(scores) / len(scores)

print(
    f"\nFinal average: "
    f"{final_average_score:.1f}"
)