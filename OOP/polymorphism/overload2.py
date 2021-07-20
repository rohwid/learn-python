class Compute:
    # area method
    def area(self, x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0

# object
obj = Compute()

# zero argument
print("Area:", obj.area())

# one argument
print("Area:", obj.area(2))

# two argument
print("Area:", obj.area(4, 5))
