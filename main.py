from library import Book, Member, Library

def main():
    library = Library()

    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    print("\nAvailable books:")
    library.show_books()

    member = Member("Alice")

    print("\nBorrowing a book:")
    member.borrow_book(library.books[0])

    print("\nAvailable books after borrowing:")
    library.show_books()

    print("\nReturning a book:")
    member.return_book(library.books[0])

    print("\nAvailable books after returning:")
    library.show_books()

if __name__ == "__main__":
    main()
