# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")
except Exception as err:
    print (err)
    raise  # To determine whether the exception was raised or not