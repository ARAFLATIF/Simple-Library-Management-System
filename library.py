class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_lent = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_lent:
            print(f"Sorry, {book.title} is currently lent out.")
        else:
            book.is_lent = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_lent = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author} to the library.")

    def show_books(self):
        for book in self.books:
            status = "Available" if not book.is_lent else "Lent out"
            print(f"{book.title} by {book.author} - {status}")
