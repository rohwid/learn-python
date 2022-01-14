class School:
    #attribute
    school_name = "ITS"

    # constructor
    def __init__(self, name, age):
        
        # public data members
        self.name = name
        self.age = age

    # public member function     
    def displayAge(self):
        
        # accessing public data member
        print("Age: ", self.age)
 
# creating object of the class
school = School("Rohman", 20)
 
# accessing public data member
print("Name: ", school.name)
 
# calling public member function of the class
school.displayAge()

# calling the attribut 
print("School: ", school.school_name)