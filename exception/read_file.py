# The default is to make error

try:
	fh = open("test_file.txt", "r")
	fh.write("This is my test file for exception handling!!")
except Exception as err:
	print(err)
else:
	print("Written content in the file successfully")
