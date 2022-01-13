import datetime

class User:
    def __init__(self, name, last_name, sex, year):
        self.__set_name(name)
        self.__set_last_name(last_name)
        self.__set_sex(sex)
        self.__set_year(year)
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
    def __str__(self):                      # napisowa reprezentacja obiektu
        return f"{self.__name} {self.__last_name} płeć: {'M' if self.__sex else 'K'} wiek: {self.get_age()}"
    name = property(__get_name, __set_name)
    last_name = property(__get_last_name, __set_last_name)
    sex = property(__get_sex, __set_sex)
    year = property(__get_year, __set_year)