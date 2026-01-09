

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self) -> str:
        return f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.isbn!r})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print(f"Added book: {book.display_info()}")

    def remove_book_by_isbn(self, isbn: str) -> bool:
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                removed = self.books.pop(i)
                print(f"Removed book: {removed.display_info()}")
                return True
        print(f"No book found with ISBN: {isbn}")
        return False

    def list_books(self) -> None:
        if not self.books:
            print("Library is empty.")
            return
        print("Listing all books in the library:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book.display_info()}")

    def search_by_title(self, query: str):
        q = query.strip().lower()
        matches = [book for book in self.books if q in book.title.lower()]
        if matches:
            print(f"Found {len(matches)} book(s) matching '{query}':")
            for book in matches:
                print(f"- {book.display_info()}")
        else:
            print(f"No books found matching title: '{query}'")
        return matches


if __name__ == "__main__":
 
    library = Library()  

    b1 = Book("The Pragmatic Programmer", "Andy Hunt & Dave Thomas", "978-0201616224")
    b2 = Book("Clean Code", "Robert C. Martin", "978-0132350884")
    b3 = Book("Introduction to Algorithms", "Cormen, Leiserson, Rivest, Stein", "978-0262033848")
    library.add_book(b1)
    library.add_book(b2)
    library.add_book(b3)

    print()  

    library.list_books()  

    print()  

    
    library.search_by_title("clean code")

    print()  

    library.remove_book_by_isbn("978-0132350884")
    print()
    library.list_books()