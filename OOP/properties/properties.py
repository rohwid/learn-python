class SoftwareEngineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary

if __name__ == "__main__":
    se = SoftwareEngineer()
    
    se.salary = 6000
    print(se.salary)
    
    del se.salary
    
    # It will return error (because deleted)
    # print(se.salary)