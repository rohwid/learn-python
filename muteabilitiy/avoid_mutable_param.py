from typing import List, Optional

class Student:
    # def __init__(self, name: str, grades: List[int] = []):
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

"""
The purpose is to script is to make the value of the object different.
"""

if __name__ == "__main__":
    bob = Student("Bob")
    rolf = Student("Rolf")
    bob.take_exam(90)
    print(bob.grades)
    print(rolf.grades)