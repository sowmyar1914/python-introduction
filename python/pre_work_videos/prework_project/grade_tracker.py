# Import Python's built-in csv module.
# We use this module to read the students.csv file.
import csv


def load_students(filepath):
    """
    Read student data from a CSV file.

    Parameters:
        filepath: the path to the CSV file

    Returns:
        A list of dictionaries.
        Each dictionary represents one student.

    If the file does not exist:
        Print a helpful error message
        Return an empty list
    """

    try:
        # Open the file in read mode.
        # "r" means we are reading from the file.
        # newline="" helps Python handle CSV line endings correctly.
        with open(filepath, "r", newline="") as file:

            # DictReader reads each CSV row as a dictionary.
            #
            # For example:
            #
            # student_name,math,science,english,history
            # Alice Johnson,92,88,95,91
            #
            # becomes approximately:
            #
            # {
            #     "student_name": "Alice Johnson",
            #     "math": "92",
            #     "science": "88",
            #     "english": "95",
            #     "history": "91"
            # }
            reader = csv.DictReader(file)

            # Convert the DictReader object into a normal Python list.
            # This list will contain one dictionary for each student.
            students = list(reader)

            # Send the student list back to the part of the program
            # that called this function.
            return students

    except FileNotFoundError:
        # This code runs if Python cannot find the CSV file.
        # Instead of crashing, we display a helpful message.
        print(f"Error: Could not find the file '{filepath}'.")

        # Return an empty list so the rest of the program
        # can handle the missing file safely.
        return []


def calculate_average(grades):
    """
    Calculate the average of a student's grades.

    Parameters:
        grades: a list of grade values

    Example:
        ["92", "88", "95", "91"]

    Missing grades may appear as empty strings:
        ["78", "82", "", "79"]

    Returns:
        A float rounded to 1 decimal place

    Returns None if the student has no valid grades.
    """

    # Create an empty list where we will store
    # only valid numeric grades.
    valid_grades = []

    # Go through every grade in the list one at a time.
    for grade in grades:

        # CSV values are read as strings.
        #
        # A missing grade looks like:
        # ""
        #
        # We only want to process grades that are not empty.
        if grade != "":

            # Convert the grade from a string to a number.
            #
            # Example:
            # "92" becomes 92.0
            numeric_grade = float(grade)

            # Add the numeric grade to our valid grades list.
            valid_grades.append(numeric_grade)

    # After checking all grades, determine whether
    # we found any valid grades.
    if len(valid_grades) == 0:

        # If there are no valid grades, we cannot calculate
        # an average.
        return None

    # Add all valid grades together.
    total = sum(valid_grades)

    # Count how many valid grades we have.
    number_of_grades = len(valid_grades)

    # Calculate the average.
    average = total / number_of_grades

    # Round the average to one decimal place.
    #
    # Example:
    # 86.666666 becomes 86.7
    average = round(average, 1)

    # Send the final average back.
    return average


def get_letter_grade(average):
    """
    Convert a numeric average into a letter grade.

    Grade scale:
        90 and above = A
        80-89.9      = B
        70-79.9      = C
        60-69.9      = D
        Below 60     = F

    If the average is None:
        Return "N/A"
    """

    # First check if the student has no numeric average.
    if average is None:
        return "N/A"

    # Check from the highest grade range to the lowest.
    if average >= 90:
        return "A"

    elif average >= 80:
        return "B"

    elif average >= 70:
        return "C"

    elif average >= 60:
        return "D"

    else:
        # If none of the conditions above were true,
        # the average must be below 60.
        return "F"


def generate_report(students):
    """
    Process all student records and create a complete report.

    The report includes:
        - total number of students
        - class average
        - highest average
        - lowest average
        - grade distribution
        - individual student results
    """

    # Create a dictionary to count how many students
    # receive each letter grade.
    #
    # All counts start at 0.
    grade_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
        "N/A": 0
    }

    # This list will store each student's final result.
    #
    # Example item:
    #
    # {
    #     "student_name": "Alice Johnson",
    #     "average": 91.5,
    #     "letter_grade": "A"
    # }
    student_results = []

    # This list will store only valid numeric averages.
    # We need these values to calculate class statistics.
    valid_averages = []

    # Process each student one at a time.
    for student in students:

        # Collect the student's four subject grades
        # into one list.
        grades = [
            student["math"],
            student["science"],
            student["english"],
            student["history"]
        ]

        # Calculate the student's numeric average.
        average = calculate_average(grades)

        # Convert the average into a letter grade.
        letter_grade = get_letter_grade(average)

        # Create a dictionary containing this student's results.
        student_result = {
            "student_name": student["student_name"],
            "average": average,
            "letter_grade": letter_grade
        }

        # Add the student's result to the full results list.
        student_results.append(student_result)

        # Increase the correct letter-grade count.
        #
        # For example:
        # if letter_grade is "A",
        #
        # grade_distribution["A"] += 1
        #
        # increases the A count by 1.
        grade_distribution[letter_grade] += 1

        # Only add real numeric averages to valid_averages.
        #
        # We do not want None values included because
        # mathematical functions cannot calculate with None.
        if average is not None:
            valid_averages.append(average)

    # Check whether there are any valid student averages.
    if valid_averages:

        # Calculate the class average.
        #
        # Add all student averages and divide by
        # the number of students with valid averages.
        class_average = sum(valid_averages) / len(valid_averages)

        # Round the class average to one decimal place.
        class_average = round(class_average, 1)

        # Find the highest student average.
        highest_average = max(valid_averages)

        # Find the lowest student average.
        lowest_average = min(valid_averages)

    else:
        # If nobody has a valid grade,
        # there are no statistics to calculate.
        class_average = None
        highest_average = None
        lowest_average = None

    # Create one dictionary that contains
    # the complete class report.
    report = {
        "total_students": len(students),
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": grade_distribution,
        "student_results": student_results
    }

    # Return the finished report.
    return report


def write_report(report, filepath):
    """
    Write the complete class report to a text file.

    Parameters:
        report: the report dictionary created by generate_report()
        filepath: the name/path of the output file

    Example output file:
        grade_report.txt
    """

    # Open the file in write mode.
    #
    # "w" means:
    # - create the file if it does not exist
    # - replace its old contents if it already exists
    with open(filepath, "w") as file:

        # Write the title of the report.
        file.write("STUDENT GRADE REPORT\n")

        # Write a divider line.
        file.write("====================\n\n")

        # -------------------------
        # SUMMARY SECTION
        # -------------------------

        file.write("SUMMARY\n")
        file.write("-------\n")

        # Write total number of students.
        file.write(
            f"Total students:   {report['total_students']}\n"
        )

        # Write class average.
        file.write(
            f"Class average:    {report['class_average']}\n"
        )

        # Write highest student average.
        file.write(
            f"Highest average:  {report['highest_average']}\n"
        )

        # Write lowest student average.
        file.write(
            f"Lowest average:   {report['lowest_average']}\n"
        )

        # Add a blank line before the next section.
        file.write("\n")

        # -------------------------
        # GRADE DISTRIBUTION
        # -------------------------

        file.write("GRADE DISTRIBUTION\n")
        file.write("------------------\n")

        # Loop through the grade distribution dictionary.
        #
        # Example:
        # grade = "A"
        # count = 3
        for grade, count in report["grade_distribution"].items():

            # Write each letter grade and its count.
            file.write(f"{grade}: {count}\n")

        # Add a blank line.
        file.write("\n")

        # -------------------------
        # INDIVIDUAL RESULTS
        # -------------------------

        file.write("INDIVIDUAL STUDENT RESULTS\n")
        file.write("--------------------------\n")

        # Go through every student result.
        for student in report["student_results"]:

            # Store each value in a shorter variable
            # to make the code easier to read.
            name = student["student_name"]
            average = student["average"]
            letter_grade = student["letter_grade"]

            # If a student has no valid grades,
            # show N/A instead of None.
            if average is None:
                average_display = "N/A"

            else:
                # Show the average with exactly one decimal place.
                #
                # Example:
                # 91.5
                average_display = f"{average:.1f}"

            # Write the student result.
            #
            # <22 means:
            # left-align the name in a 22-character field
            #
            # >5 means:
            # right-align the average in a 5-character field
            #
            # This helps the report columns line up neatly.
            file.write(
                f"{name:<22} "
                f"{average_display:>5} "
                f"({letter_grade})\n"
            )


# ---------------------------------------------------------
# IMPORTANT:
# If your instructor already gave you the main() function,
# KEEP THEIR VERSION.
# Do not replace or modify it.
#
# The code below is only a full example of how the program
# could run.
# ---------------------------------------------------------

def main():

    # Tell the user that the program is starting
    # to load student data.
    print("Loading student data...")

    # Read student data from the CSV file.
    students = load_students("data/students.csv")

    # If the list is empty, no students were loaded.
    if not students:
        print("No student data was loaded.")
        return

    # Display how many students were loaded.
    print(f"  Loaded {len(students)} students.")

    # Tell the user the report is being generated.
    print("\nGenerating report...")

    # Generate the complete class report.
    report = generate_report(students)

    # -------------------------
    # DISPLAY SUMMARY
    # -------------------------

    print("\n--- Summary ---")

    print(
        f"Total students:   {report['total_students']}"
    )

    print(
        f"Class average:    {report['class_average']}"
    )

    print(
        f"Highest average:  {report['highest_average']}"
    )

    print(
        f"Lowest average:   {report['lowest_average']}"
    )

    # -------------------------
    # DISPLAY GRADE DISTRIBUTION
    # -------------------------

    print("\nGrade Distribution:")

    for grade, count in report["grade_distribution"].items():
        print(f"  {grade}: {count}")

    # -------------------------
    # FIND TOP 5 STUDENTS
    # -------------------------

    print("\nTop 5 students:")

    # Create a new list that contains only students
    # with valid numeric averages.
    valid_students = [
        student
        for student in report["student_results"]
        if student["average"] is not None
    ]

    # Sort students by average from highest to lowest.
    #
    # reverse=True means descending order.
    sorted_students = sorted(
        valid_students,
        key=lambda student: student["average"],
        reverse=True
    )

    # [:5] means only take the first five students.
    for student in sorted_students[:5]:

        print(
            f"  {student['student_name']:<20} "
            f"{student['average']:.1f} "
            f"({student['letter_grade']})"
        )

    # Write the full report to grade_report.txt.
    write_report(
        report,
        "grade_report.txt"
    )

    # Confirm that the report file was created.
    print("\nReport written to grade_report.txt")


# This condition makes main() run when you execute:
#
# python grade_tracker.py
#
# It prevents main() from automatically running
# if this file is imported into another Python program.
if __name__ == "__main__":
    main()