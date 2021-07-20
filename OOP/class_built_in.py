class Employee:
    empCount = 0

    # contructor -> __init__(self, param-1, ...param-n)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # count object as employee
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee ", self.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

# check class built in
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
