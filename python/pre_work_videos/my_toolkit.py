# my_toolkit.py 
def calculate_average(numbers):
    """Calculate the average of a list of numbers and returns average, Returns 0 if the list is empty."""

    if len(numbers) == 0:
        return 0
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)
    return average
def find_max_and_min(numbers):
    """Takes a list of numbers, returns a tuple (max_value, min_value). Do NOT use the built-in max() and min() — implement the logic yourself with a loop."""

    if len(numbers) == 0:
        return (None, None)
    max_value = numbers[0]
    min_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    return (max_value, min_value)

def count_occurrences(items, target):
   """ Takes a list and a target value, returns how many times the target appears in the list. Do NOT use the built-in .count() method.""" 
   count = 0
   for item in items:

        if item == target:
            count = count + 1

   return count



def is_palindrome(text):
    """Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces). Examples: "racecar" → True, "hello" → False, "A man a plan a canal Panama" → True."""
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    # Check if the cleaned text is the same forwards and backwards
    reversed_text = cleaned_text[::-1]
    if cleaned_text == reversed_text:
        return True
    else:
        return False

def create_report(title, scores):
        """Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally. Returns a formatted string report (NOT a print — a return)."""
        average = calculate_average(scores)
        max_score, min_score = find_max_and_min(scores)
        report = (
            f"=== {title} ===\n"
            f"Average Score: {average:.2f}\n"
            f"Max Score: {max_score}\n"
            f"Min Score: {min_score}"
        )
        return report
    #test section 
if __name__ == "__main__":
    # Test the functions
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    # edge case tests
    print()
    print("=====EDGE CASE TESTS=====")
    # empty list for average
    print(f"Average of empty list: {calculate_average([])}")
    # empty list for max/min
    print(f"Max/Min of empty list: {find_max_and_min([])}")
    # target  appears multiple times in the list
    repeated_list = [5, 2, 5, 7, 5, 9, 5]
    print(f"Count of 5 in repeated list: {count_occurrences(repeated_list, 5)}")
    # target doesnot appear in the list
    print(f"Count of 10 in repeated list: {count_occurrences(repeated_list, 10)}")
    # phrase with spaces 
    print(f"'A man a plan a canal Panama' palindrome: {is_palindrome('A man a plan a canal Panama')}")
    # single character
    print(f"'A' palindrome: {is_palindrome('A')}")
    # mixxed upper case and lower case 
    print(
        f"'RaceCar' palindrome: "
        f"{is_palindrome('RaceCar')}"
    )
    # empty string
    print(
        f"Empty string palindrome:"
        f"{is_palindrome('')}"
    )

          

