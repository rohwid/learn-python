from typing import List

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, books_type, weight: int):
        self.name = name
        self.books_type = books_type
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.books_type}, weighing {self.weight} g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)