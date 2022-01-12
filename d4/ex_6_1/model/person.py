class Person:
    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address
    def to_csv(self):
        return f"{self.name};{self.last_name};{self.address.to_csv()}"
    def __str__(self):
        return f"imię: {self.name} nazwisko: {self.last_name} adres: {self.address}"
