class Employee:
    def __init__(self, name, last_name, income):
        self.name = name
        self.last_name = last_name
        self.income = income
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.name} {self.last_name} zarobki: {self.income}zł"

class Manager(Employee):
    def __init__(self, name, last_name, income, role):
        super().__init__(name, last_name, income)
        self.role = role
        self.employees = []
    def add_employee(self, employee):
        if employee is not self.employees:
            self.employees.append(employee)
    def remove_employee(self, index):
        self.employees.remove(self.employees[index])
    def __str__(self):
        return super().__str__() + f" rola: {self.role} zaspół: {[empl.__str__() for empl in self.employees]}"

e1 = Employee('Jan', 'Kowalski', 4_000)
print(e1)

m1 = Manager("Adam", "Nowak", 14000, "IT")
m1.add_employee(e1)
m1.add_employee(Employee('Janusz','Kot',5000))
print(m1)
m1.remove_employee(0)
print(m1)

m2 = Manager("Andrzej", "Kolejny", 14000, "DEV OPS")
print(m2)
