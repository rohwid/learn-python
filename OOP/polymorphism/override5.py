# Parent class
class Awesome:
    # Main method
    def greetings(self, message = "Hello World"):
        print("Greetings from Awesome:", message)

# Child class
class SuperAwesome(Awesome):
    # Overriding the method of the parent class
    def greetings(self, message = None):

        if message != None:
            print("Greetings from SuperAwesome:", message)

            # Calling the overridden parent class greetings method
            super().greetings(message)

        else:
            print("Greetings from SuperAwesome!")

# Objects
cObj = SuperAwesome()   # Child class object

# Method call
cObj.greetings()
cObj.greetings('Hello!')
