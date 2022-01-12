from d4.ex_6_1.model.address import Address
from d4.ex_6_1.model.person import Person

if __name__ == '__main__':
    a1 = Address("Królewska 3", "00-001", "Warszawa")
    a2 = Address("Długa 1", "00-101", "Warszawa")
    p1 = Person("Adam", "Kowalski", a1)
    p2 = Person("Anna", "Kowalska", a1)
    p3 = Person("Jan", "Nowak", a2)
    print(p1)
    print(p2)
    print(p3)
    print(p1.to_csv())