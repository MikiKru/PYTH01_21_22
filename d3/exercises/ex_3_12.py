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


# lista mężczyzn z danego miasta
# SELECT * FROM users WHERE address[1] = 'Gdańsk';
city = "Gdańsk"
users_from_city = [user for user in users if user['address'][0] == city]
# for user in users:
#     if user['address'][0] == city:
#         users_from_city.append(user)

print("###########")
for user in users_from_city:
    print(f"|{user['name']:>15}|{user['last_name']:>15}|{user['address'][0]:>15}|{user['address'][1]:>35}|{user['address'][2]:5}|{user['gender']:5}|{user['age']:5}|")

# lista osób z danego przedziału wiekowego
# SELECT * FROM users WHERE age BETWEEN 40 AND 60;
# age_between = range(40, 61)
users_from_age = [user for user in users if user['age'] in range(40, 61)]
# for user in users:
#     if user['age'] in age_between:
#         users_from_age.append(user)
print("###########")
for user in users_from_age:
    print(f"|{user['name']:>15}|{user['last_name']:>15}|{user['address'][0]:>15}|{user['address'][1]:>35}|{user['address'][2]:5}|{user['gender']:5}|{user['age']:5}|")

# średnia wieku kobiet o imionach rozpoczynających się na A
# SELECT avg(age) FROM users WHERE gender = 0 AND name like 'A%';
women_starts_from_A = [user['age'] for user in users if user['name'][0] == "A" and not user['gender']]
print("###########")
print("Średnia wieku: ", round(mean(women_starts_from_A), 2))
print("Standardowe odchylenie: ", round(stdev(women_starts_from_A), 2))