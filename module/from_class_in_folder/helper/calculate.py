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