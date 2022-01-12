import datetime

class User:
    def __init__(self, name, last_name, sex, year):
        self.__name = name              # pole silnie prywatne -> niedostępne spoza klasy
        self.__last_name = last_name
        self.__sex = sex
        self.__year = year
    def get_age(self):
        return datetime.date.today().year - self.__year
    def set_year(self, year):
        if str(type(year)) == "<class 'int'>":
            print("zaktualizowano wartość")
            self.__year = year
        else:
            print("błędny typ wartości - pole pozostaje bez zmian!")

    def get_year(self):
        return self.__year
    def __str__(self):                      # napisowa reprezentacja obiektu
        return f"{self.__name} {self.__last_name} płeć: {'M' if self.__sex else 'K'} wiek: {self.get_age()}"

u1 = User("Adam", "Kowalski", True, 1990)
u1.set_year(u1.get_year() + 1)
u1.set_year("1410")             # walidacja!!!
print(u1)

