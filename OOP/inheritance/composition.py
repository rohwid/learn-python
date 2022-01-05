class BookShelf:
    def __init__(self, *book):
        self.book = book
    
    def __str__(self):
        return f'Bookself with {len(self.book)} of books'

    def title(self, number):
        return f'{self.book[number]}'

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'The book title is {self.name}'

book1 = Book('Python 101')
print(book1)

book2 = Book('Flask 101')
print(book2)

shelf = BookShelf(book1, book2)
print(shelf)

print(shelf.title(0))