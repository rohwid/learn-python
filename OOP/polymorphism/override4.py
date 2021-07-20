# Parent class
class Awesome:
    # Main method
    def greetings(self, message = "Hello World"):
        print("Greetings from Awesome:", message)

# Child class
class SuperAwesome(Awesome):
    # Overriding the method of the parent class
    def greetings(self, message=None):
        if message != None:
            print("Greetings from SuperAwesome:", message)
        else:
            print("Greetings from SuperAwesome!")

# Objects
pObj = Awesome()        # Parent class object
cObj = SuperAwesome()   # Child class object

# method call
pObj.greetings()
pObj.greetings('Hello!')

cObj.greetings()
cObj.greetings('Hello!')
