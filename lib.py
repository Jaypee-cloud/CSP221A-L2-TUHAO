class BookUnavailableError(Exception):
    pass


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_checked_out = False

    def __str__(self):
        if self.is_checked_out:
            status = "Checked out"
        else:
            status = "Available"

        return f"{self.title} - {status}"


class Member:
    def __init__(self, name):
        self.name = name

    def borrow(self, book):
        if book.is_checked_out:
            raise BookUnavailableError(
                f"'{book.title}' is already checked out."
            )

        book.is_checked_out = True
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        book.is_checked_out = False
        print(f"{self.name} returned '{book.title}'.")


book = Book("Python Basics", "12345")
member = Member("John")

print(book)

# Successful borrow
member.borrow(book)
print(book)

# Successful return
member.return_book(book)
print(book)

# Borrow again
member.borrow(book)

# Failed borrow
try:
    member.borrow(book)
except BookUnavailableError as e:
    print("Error:", e)