class Parent:
    def myMethod(self):
        print('Calling parent method')

class Child(Parent):
    # Overide
    def myMethod(self):
        print('Calling child method')

# Call overiding class
c = Child()
c.myMethod()
