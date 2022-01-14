class Parent:
    parent_attr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parent_method(self):
        print("Calling parent method")

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print("Parent attribute :", Parent.parent_attr)

# inherit
class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def child_method(self):
        print("Calling child method")

    def get_parent_attr(self):
        print("Child attribute :", Parent.parent_attr)

c = Child()
c.child_method()
c.parent_method()
c.set_attr(200)
c.get_attr()
c.get_parent_attr()
