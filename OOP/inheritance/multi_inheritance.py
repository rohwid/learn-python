class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city
        
class Student(Person, Address):
    def __init__(self, fname, lname, street, city, year):
        Person.__init__(self, fname, lname)
        Address.__init__(self, street, city)
        self.graduationyear = year
        
    def welcome(self):
        print(f'Hello {self.firstname} {self.lastname}, student - graduate on {self.graduationyear}')


x = Student("Rohman", "Widiyanto", "Jalan Buntu No. 666", "Jakarta", 2022)

x.welcome()
print(x.street)
print(x.city)
