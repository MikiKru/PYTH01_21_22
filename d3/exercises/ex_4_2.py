from statistics import mean, stdev

p1 = {"name": "Adam", "last_name": "Kowalski", "address": ("Warszawa", "Królewska", 15), "gender": True, "age": 39}
p2 = {"name": "Benek", "last_name": "Benkowski", "address": ("Jaroty", "Bartąska", 128), "gender": True, "age": 45}
p3 = {"name": "Andrzej", "last_name": "Spirytus", "address": ("Gdańsk", "Zbójnicka", 2), "gender": True, "age": 35}
p4 = {'name': 'Anna', 'last_name': 'Nowak', 'address': ('Gdynia', 'Morska', 32), 'gender': False, 'age': 27}
p5 = {"name": "Piotr", "last_name": "Sosiński", "address": ("Derc", "Bobrowa", 128), "gender": True, "age": 51}
p6 = {"name": "Jan,", "last_name": "Jankowski", "address": ("Gdańsk", "Towarowa", 38), "gender": True, "age": 30}
p7 = {"name": "Woyt", "last_name": "Brozyna", "address": ("Pcim koło warszawki", None, 1), "gender": True, "age": 75}
p8 = {"name": "Aleksandra", "last_name": "Kowalska", "address": ("Gdańsk", "Zbożowa", 4), "gender": False, "age": 40}

users = [p1, p2, p3, p4, p5, p6, p7, p8]
# predykaty -> zwracają wartość logiczną i przyjmują w argumencie pojedynczy element sekwencji którą mają filtrować
def is_user_from_city(user):
    if user['address'][0] == "Gdańsk":
        return True
    return False
def is_user_age_in_range(user):
    if user['age'] in range(40,61):
        return True
    return False
def is_woman_and_name_starts_with_a(user):
    if user['name'][0] == "A" and not user['gender']:
        return True
    return False

# fukcje przyjmujące w argimencie obiekt innej fukcji - predykatu mogą na podstawie tego obiektu wywoływać funkcje predykaty w dowolnym momencie
# def get_users_from_city(predicate, users):
#     return [user for user in users if predicate(user)]
# def get_users_with_age_in_range(predicate, users):
#     return [user for user in users if predicate(user)]
# def get_women_and_name_starts_with_a(predicate, users):
#     return [user for user in users if predicate(user)]
def f(predicate, users):
    return [user for user in users if predicate(user)]

print(f(is_user_from_city, users))
print(f(is_user_age_in_range, users))
print(f(is_woman_and_name_starts_with_a, users))

