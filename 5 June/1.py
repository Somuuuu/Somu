class Book:
    def __init__(self, name, stock, id):
        self.id = id
        self.name = name
        self.stock = stock
class Library:
    def __init__(self, books):
        self.books = books
        
    def issue_book(self, id):
        for book in self.books:
            if book.id == id:
                if book.stock >=1:
                    book.stock -= 1
                    return f"Book issued, '{book.name}'"
                else:
                    return "Sorry no stock"
        else:
            return f"Book with id: '{book.id}' not found"
    
    def collect_book(self, id):
        for book in self.books:
            if book.id == id:
                book.stock += 1
                return f"Book collected, {book.name}"
            else:
                return "This book is not from our library"

 
book_1 = Book("Atomic Structures", 10, 123)
book_2 = Book("Rich dad poor dad", 2, 456)
library = Library([book_1, book_2])

print("No.of available books in stock:",library.books[1].stock)
print(library.issue_book(456))
print("Remaining books available in stock:",library.books[1].stock)

print("Available books in stock:",library.books[0].stock)
print(library.collect_book(123))
print(f"Updated books in stock after collecting book:",library.books[0].stock)

 
