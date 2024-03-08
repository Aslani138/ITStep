import json

class Book:
    def __init__(self, title, author, year):
        # Initialize a Book instance with title, author, and publication year.
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # String representation of the Book instance.
        return f"'{self.title}' by {self.author}, {self.year}"

class BookManager:
    def __init__(self, filename='books.json'):
        # Initialize the BookManager, loading books from a JSON file.
        self.books = []  # List to store Book instances.
        self.filename = filename  # JSON file for storing books data.
        self.load_books()  # Load books from the JSON file.

    def add_book(self, book):
        # Add a Book instance to the manager and save to JSON file.
        self.books.append(book)
        self.save_books()

    def show_books(self):
        # Print all books in the manager.
        for book in self.books:
            print(book)

    def search_books(self, title):
        # Search for books by title (case-insensitive).
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books

    def save_books(self):
        # Save the list of books to a JSON file.
        with open(self.filename, 'w') as f:
            json.dump([book.__dict__ for book in self.books], f)

    def load_books(self):
        # Load books from the JSON file.
        try:
            with open(self.filename, 'r') as f:
                books_data = json.load(f)
                for book_data in books_data:
                    self.books.append(Book(**book_data))
        except FileNotFoundError:
            # If no JSON file exists, start with an empty book list.
            self.books = []

def main():
    # Main function to run the book manager.
    manager = BookManager()

    while True:
        # User interface for managing books.
        print("\nBook Manager")
        print("1. Add a new book")
        print("2. Show all books")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new book to the manager.
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")

            # Validate user input.
            if not title or not author or not year.isdigit():
                print("Invalid input. Please try again.")
                continue

            book = Book(title, author, int(year))
            manager.add_book(book)
            print("Book added successfully.")

        elif choice == "2":
            # Display all books.
            print("\nList of all books:")
            manager.show_books()

        elif choice == "3":
            # Search for a book by title.
            search_title = input("Enter book title to search: ")
            found_books = manager.search_books(search_title)
            if found_books:
                print("\nFound Books:")
                for book in found_books:
                    print(book)
            else:
                print("No books found with that title.")

        elif choice == "4":
            # Exit the program.
            print("Exiting program.")
            break

        else:
            # Handle invalid choice.
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
