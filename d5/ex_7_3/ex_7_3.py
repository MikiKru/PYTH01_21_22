from d4.ex_6_1.model.address import Address
from d4.ex_6_1.model.person import Person

class IOOperations:
    def __init__(self):
        a1 = Address("Królewska 3", "00-001", "Warszawa")
        a2 = Address("Długa 1", "00-101", "Warszawa")
        p1 = Person("Adam", "Kowalski", a1)
        p2 = Person("Anna", "Kowalska", a1)
        p3 = Person("Jan", "Nowak", a2)
        self.people = [p1, p2, p3]
    def save_to_file(self, path):
        with open(path, mode='w', encoding="utf-8") as p_file:
            p_file.write("name;lastname;street;postal code;city\n")
            for p in self.people:
                p_file.write(p.to_csv() + "\n")
    def read_from_file(self, path):
        with open(path, mode='r', encoding="utf-8") as p_file:
            for index, line in enumerate(p_file.readlines()):
                if not index:
                    continue
                # mapowanie wiersza z pliku na obiekt person
                col = str(line.strip()).split(";")
                p = Person(col[0], col[1], Address(col[2], col[3], col[4]))
                self.people = []
                self.people.append(p)
                self.print_people()
    def print_people(self):
        for person in self.people:
            print(person)

ioo = IOOperations()
ioo.save_to_file(r'files\people.csv')
ioo.read_from_file(r'files\people.csv')