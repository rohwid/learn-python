# Raise uses to throw an exception if a condition occurs.
x = "hello"

if not type(x) is int:
    # Must be use the TYPE OF EXCEPTION
    raise TypeError("Only integers are allowed")