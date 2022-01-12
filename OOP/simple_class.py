class Employee:
    # alias
    company_name = "Pacmann"
    emp_count = 0

    # contructor -> __init__(self, param-1, ...param-n)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # count object as employee
        Employee.emp_count += 1

    def displayCount(self):
        print("Total Employee ", self.emp_count)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

# create instance
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp3 = Employee("Larsson", 15000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

print("\nCompany Name: ", Employee.company_name)
print("Total Employee: ", Employee.emp_count)
