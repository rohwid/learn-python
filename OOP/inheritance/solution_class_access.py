class Bookself:
    def __init__(self, quantitiy):
        self.quantity = quantitiy
    
    def __str__(self):
        return f'Bookself with {self.quantity} of books'

class Book(Bookself):
    def __init__(self, name, quantitiy):
        super().__init__(quantitiy)
        self.name = name
    
    def __str__(self):
        return f'Books with name {self.quantity} are {self.quantity} unit'

book = Book('Python 101', 100)
print(book)
