from d4.ex_6_1.model.address import Address
from d4.ex_6_1.model.person import Person

a1 = Address("Królewska 3", "00-001", "Warszawa")
a2 = Address("Długa 1", "00-101", "Warszawa")
p1 = Person("Adam", "Kowalski", a1)
p2 = Person("Anna", "Kowalska", a1)
p3 = Person("Jan", "Nowak", a2)

people = [p1, p2, p3]

with open(r'files\people.csv', mode='w', encoding="utf-8") as p_file:
    for p in people:
        p_file.write(p.to_csv() + "\n")