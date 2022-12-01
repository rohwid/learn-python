from helper.calculate import Employee

if __name__ == "__main__":
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    emp3 = Employee("Larsson", 15000)

    emp1.displayEmployee()
    emp2.displayEmployee()
    emp3.displayEmployee()

    print("\nCompany Name: ", Employee.company_name)
    print("Total Employee: ", Employee.emp_count)