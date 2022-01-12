class User:
    # składowe statyczne - wartość zainicjalizowana dla każdego użytkownika
    role = 'USER'

    def __init__(self, name, last_name, email, password):     # metoda inicjalizująca obiekt klasy -> nadaje warunki początkowe
        self.name = name # przypisz WAROTSC do pola klasowego dla danego obiektu
        self.last_name = last_name
        self.email = email
        self.password = password
        self.emails_history = []
        self.emails_history.append(email)
    def set_email(self, email):
        self.email = email
        self.emails_history.append(self.email)
    def get_user(self):
        return f"role={self.role} name={self.name} last_name={self.last_name} email={self.email} emails={self.emails_history}"

user1 = User("Michał", "Kruczkowski", "mk@mk.pl", "mk")
user1.set_email("x@x.pl")
user1.set_email("x@x.pl")

user2 = User("A", "A", "a@a.pl", "a")
user3 = User("B", "B", "b@b.pl", "b")

users = [user1, user2, user3]


for user in users:
    print(user.last_name)
# sprawdzanie przynależności obiektu do klasy
print(isinstance(user1, User))
print(isinstance(user1, object))
print(user1.__dict__)
