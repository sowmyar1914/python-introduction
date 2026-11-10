
# Module 2 - Dunder Methods Deep Dive
# This program shows how special methods work in a Book class.


class Book:

    # This method creates a new book object
    def __init__(self, title, author, year, pages):

        # Check if the year is a positive integer
        if type(year) != int or year <= 0:
            raise ValueError("Year must be a positive integer")

        # Store the book information
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

        # A new book is available at first
        self.checked_out = False

    # This method allows us to compare two books using ==
    def __eq__(self, other):

        # Check if both objects are books
        if isinstance(other, Book):

            # Compare books using title and author
            return (self.title == other.title and
                    self.author == other.author)

        return NotImplemented

    # This method allows us to sort books using <
    def __lt__(self, other):

        # Check if both objects are books
        if isinstance(other, Book):

            # Compare book titles in alphabetical order
            return self.title < other.title

        return NotImplemented

    # This method returns the number of pages
    def __len__(self):

        # Return the total pages in the book
        return self.pages

    # This method searches for a keyword in the book title
    def __contains__(self, keyword):

        # Convert both words to lowercase before searching
        return keyword.lower() in self.title.lower()

    # This method checks out a book
    def check_out(self):

        # Check if the book is available
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out")
        else:
            print(f"{self.title} is already checked out")

    # This method returns a book
    def return_book(self):

        # Check if the book was borrowed
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not checked out")

    # This method shows book information when printed
    def __repr__(self):

        # Check the status of the book
        if self.checked_out:
            status = "Checked Out"
        else:
            status = "Available"

        return f"{self.title} by {self.author} - {status}"


# --------------------------------
# Testing the Dunder Methods
# --------------------------------

# Create four book objects
book1 = Book("Python Crash Course", "Eric Matthes", 2019, 544)
book2 = Book("Clean Code", "Robert Martin", 2008, 464)
book3 = Book("AI Engineering", "Chip Huyen", 2025, 540)
book4 = Book("Python Crash Course", "Eric Matthes", 2022, 600)


# Test 1 - Compare two books using ==
print("\nTesting __eq__:")

# These books have the same title and author
print(book1 == book4)

# These books have different titles and authors
print(book1 == book2)


# Test 2 - Compare two books using <
print("\nTesting __lt__:")

# Check if the first title comes before the second
print(book2 < book1)


# Test 3 - Find the number of pages using len()
print("\nTesting __len__:")

print(f"Pages in {book1.title}: {len(book1)}")


# Test 4 - Search for a keyword using in
print("\nTesting __contains__:")

# Check if Python appears in the book title
print("python" in book1)

# Check if Java appears in the book title
print("java" in book1)


# Test 5 - Sort books alphabetically by title
print("\nSorting Books by Title:")

# Create a list of books
books = [book1, book2, book3, book4]

# sorted() uses the __lt__ method automatically
sorted_books = sorted(books)

# Print books in alphabetical order
for book in sorted_books:
    print(book)


# Test 6 - Check out and return a book
print("\nTesting Book Checkout:")

book1.check_out()
book1.return_book()


# Test 7 - Check invalid year
print("\nTesting Invalid Year:")

try:
    invalid_book = Book("Test Book", "Test Author", -2020, 100)

except ValueError as error:
    print(error)
