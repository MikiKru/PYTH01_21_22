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
print(user1.get_user())

user2 = User("A", "A", "a@a.pl", "a")
print(user2.get_user())

