import datetime

class User:
    def __init__(self, name, last_name, sex, year):
        self.__name = name              # pole silnie prywatne -> niedostępne spoza klasy
        self.__last_name = last_name
        self.__sex = sex
        self.__year = year
    def __get_name(self):
        return self.__name
    def __get_last_name(self):
        return self.__last_name
    def __get_sex(self):
        return self.__sex
    def __get_year(self):
        return self.__year
    def __set_name(self, name):
        self.__name = name
    def __set_last_name(self, last_name):
        self.__last_name = last_name
    def __set_sex(self, sex):
        self.__sex = sex
    def __set_year(self, year):
        if str(type(year)) == "<class 'int'>":
            print("zaktualizowano wartość")
            self.__year = year
        else:
            print("błędny typ wartości - pole pozostaje bez zmian!")
    def get_age(self):
        return datetime.date.today().year - self.__year
    def __eq__(self, other):
        print("wywołanie metody eq na znaku ==")
        return self.__name == other.__name and self.last_name == other.__last_name and self.__class__ == other.__class__
    def __gt__(self, other):
        print("wywołanie metody eq na znaku >")
        if self.last_name > other.__last_name:
            return True
        elif self.last_name < other.__last_name:
            return False
        else:
            if self.name > other.__name:
                return True
            else:
                return False
    def __str__(self):                      # napisowa reprezentacja obiektu
        return f"{self.__name} {self.__last_name} płeć: {'M' if self.__sex else 'K'} wiek: {self.get_age()}"
    name = property(__get_name, __set_name)
    last_name = property(__get_last_name, __set_last_name)
    sex = property(__get_sex, __set_sex)
    year = property(__get_year, __set_year)

# u1 = User("Jan", "Kowalski", True, 1990)
# u2 = User("Adam", "Kowalski", True, 1991)
# u3 = User("Anna", "Nowak", False, 1990)
#
# print(u1 == u2)
# print(u1 > u2)
# print(u2 > u3)
