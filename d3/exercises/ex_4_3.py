from statistics import mean

p1 = {"name": "Adam", "last_name": "Kowalski", "address": ("Warszawa", "Królewska", 15), "gender": True, "age": 39}
p2 = {"name": "Benek", "last_name": "Benkowski", "address": ("Jaroty", "Bartąska", 128), "gender": True, "age": 45}
p3 = {"name": "Andrzej", "last_name": "Spirytus", "address": ("Gdańsk", "Zbójnicka", 2), "gender": True, "age": 35}
p4 = {'name': 'Anna', 'last_name': 'Nowak', 'address': ('Gdynia', 'Morska', 32), 'gender': False, 'age': 27}
p5 = {"name": "Piotr", "last_name": "Sosiński", "address": ("Derc", "Bobrowa", 128), "gender": True, "age": 51}
p6 = {"name": "Jan,", "last_name": "Jankowski", "address": ("Gdańsk", "Towarowa", 38), "gender": True, "age": 30}
p7 = {"name": "Woyt", "last_name": "Brozyna", "address": ("Pcim koło warszawki", None, 1), "gender": True, "age": 75}
p8 = {"name": "Aleksandra", "last_name": "Kowalska", "address": ("Gdańsk", "Zbożowa", 4), "gender": False, "age": 40}
users = [p1, p2, p3, p4, p5, p6, p7, p8]

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
def get_age(user):
    return user["age"]
def is_man(user):
    return user['gender']

print(*filter(is_user_from_city, users))
print(*filter(is_user_age_in_range, users))
print(mean(map(get_age, filter(is_woman_and_name_starts_with_a, users))))
print(len(list(filter(is_man, users))))