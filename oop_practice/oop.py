
# Module 2 - Build a Library Catalog
# This program uses classes to manage books in a library.


# Book class stores information about a physical book
class Book:

    # This method runs when we create a new book
    def __init__(self, title, author, year):

        # Check if the year is a positive integer
        if type(year) != int or year <= 0:
            raise ValueError("Year must be a positive integer")

        # Store the book information
        self.title = title
        self.author = author
        self.year = year

        # A new book is available at first
        self.checked_out = False

    # This method checks out a book
    def check_out(self):

        # Check if the book is already borrowed
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out")
        else:
            print(f"{self.title} is already checked out")

    # This method returns a borrowed book
    def return_book(self):

        # Check if the book was borrowed
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned")
        else:
            print(f"{self.title} was not checked out")

    # This method shows book information when printed
    def __repr__(self):

        # Decide the status of the book
        if self.checked_out:
            status = "Checked Out"
        else:
            status = "Available"

        return f"{self.title} by {self.author} - {status}"


# EBook inherits from the Book class
class EBook(Book):

    # This method creates an ebook
    def __init__(self, title, author, year, file_size_mb):

        # Use the Book class to set common information
        super().__init__(title, author, year)

        # Store the ebook file size
        self.file_size_mb = file_size_mb

        # Count how many people borrowed the ebook
        self.checkout_count = 0

    # This method allows multiple ebook checkouts
    def check_out(self):

        # Increase the count each time someone borrows it
        self.checkout_count += 1

        print(f"{self.title} ebook has been checked out")

    # This method returns one borrowed ebook copy
    def return_book(self):

        # Reduce the count when someone returns it
        if self.checkout_count > 0:
            self.checkout_count -= 1
            print(f"{self.title} ebook has been returned")
        else:
            print(f"{self.title} was not checked out")

    # This method shows ebook information
    def __repr__(self):

        return (f"{self.title} by {self.author} - "
                f"{self.file_size_mb} MB - "
                f"Borrowed by {self.checkout_count} people")


# Catalog class manages all the books
class Catalog:

    # This method creates an empty catalog
    def __init__(self):

        # Store all books in a list
        self.books = []

    # This method adds a book to the catalog
    def add_book(self, book):

        # Add the book to the list
        self.books.append(book)

    # This method searches books by author
    def search_by_author(self, author):

        # Create a list to store matching books
        results = []

        # Go through each book in the catalog
        for book in self.books:

            # Compare author names without case sensitivity
            if book.author.lower() == author.lower():
                results.append(book)

        return results

    # This method searches books by title
    def search_by_title(self, keyword):

        # Create a list for matching books
        results = []

        # Check every book title
        for book in self.books:

            # Find the keyword anywhere in the title
            if keyword.lower() in book.title.lower():
                results.append(book)

        return results

    # This method finds all available books
    def get_available(self):

        # Create a list for available books
        available = []

        # Check each book in the catalog
        for book in self.books:

            # Ebooks can be borrowed by multiple people
            if isinstance(book, EBook):
                available.append(book)

            # Physical books must not be checked out
            elif not book.checked_out:
                available.append(book)

        return available

    # This method prints a summary of the catalog
    def summary(self):

        # Count all books
        total = len(self.books)

        # Count available books
        available = len(self.get_available())

        print("\nLibrary Catalog Summary")
        print(f"Total Books: {total}")
        print(f"Available Books: {available}")

        # Display each book in the catalog
        for book in self.books:
            print(book)


# -----------------------------
# Testing the Library Catalog
# -----------------------------

# Create a new empty catalog
catalog = Catalog()

# Add two physical books and one ebook
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))


# Test 1 - Search for a book by title
print("\nSearch by Title:")
results = catalog.search_by_title("python")
print(results)


# Test 2 - Search for a book by author
print("\nSearch by Author:")
results = catalog.search_by_author("Eric Matthes")
print(results)


# Test 3 - Check out a physical book
print("\nChecking Out a Book:")
catalog.books[0].check_out()


# Test 4 - Find available books
available = catalog.get_available()
print(f"Available: {len(available)} books")


# Test 5 - Check out an ebook multiple times
print("\nChecking Out an EBook:")
catalog.books[2].check_out()
catalog.books[2].check_out()


# Test 6 - Return the physical book
print("\nReturning a Book:")
catalog.books[0].return_book()


# Test 7 - Return one ebook checkout
print("\nReturning an EBook:")
catalog.books[2].return_book()


# Test 8 - Print the catalog summary
catalog.summary()


# Test 9 - Check invalid publication year
print("\nTesting Invalid Year:")

try:
    invalid_book = Book("Test Book", "Test Author", -2020)

except ValueError as error:
    print(error)
