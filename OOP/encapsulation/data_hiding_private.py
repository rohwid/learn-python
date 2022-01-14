class School:
	
	# private members
	__school_name = "ITS"

	# constructor
	def __init__(self, name, id_num, branch):
		self.__name = name
		self.__id_num = id_num
		self.__branch = branch

	# private member function
	def __display_details(self):
		
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__id_num)
		print("Branch: ", self.__branch)
	
	# public member function
	def access_private_function(self):
			
		# accesing private member function
		self.__display_details()

# creating object
school = School("R2J", 1706256, "Information Technology")

# calling public member function of the class
school.access_private_function()

# calling the attribut 
print("School Name: ", School._School__school_name)
