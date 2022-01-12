import datetime

class User:
    def __init__(self, name, last_name, sex, year):
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.year = year
    def get_age(self):
        return datetime.date.today().year - self.year
    def __str__(self):                      # napisowa reprezentacja obiektu
        return f"{self.name} {self.last_name} płeć: {'M' if self.sex else 'K'} wiek: {self.get_age()}"

u1 = User("Adam", "Kowalski", True, 1990)
u1.year += 1
print(u1)

