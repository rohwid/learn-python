class Student:
	
	# protected data members
	_school_name = "ITS"

	# constructor
	def __init__(self, name, id_num, branch):
		self._name = name
		self._id_num = id_num
		self._branch = branch
	
	# protected member function
	def _display_roll_and_branch(self):

		# accessing protected data members
		print("ID: ", self._id_num)
		print("Branch: ", self._branch)


# derived class
class School(Student):

    # constructor
    def __init__(self, name, id_num, branch):
        Student.__init__(self, name, id_num, branch) # can be change to `super().__init__(name, id_num, branch)`

    # public member function
    def display_details(self):
        # accessing protected data members of super class
        print("Name: ", self._name)
    
        # accessing protected member functions of super class
        self._display_roll_and_branch()

# creating objects of the derived class	
school = School("Rohman", 1706256, "Information Technology")

# calling public member functions of the class
school.display_details()

# calling the attribut 
print("School Name: ", Student._school_name)
