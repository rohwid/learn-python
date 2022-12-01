# NOTES:
# _var_name  : protected (can inherits or access from child class)
#              See: _salary and _num_bug_solved

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bug_solved = 0

    def code(self):
        self._num_bug_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        self._salary = self.calculate_salary(base_value)
    
    def calculate_salary(self, base_value):
        if self._num_bug_solved < 10:
            return base_value
        if self._num_bug_solved < 100:
            return base_value * 2
        return base_value * 3


if __name__ == "__main__":
    se = SoftwareEngineer("Max", 25)
    print(se.age, se.name)

    for i in range(70):
        se.code()

    se.set_salary(6000)
    print(se.get_salary())
