p1 = {"name": "Adam", "last_name": "Kowalski", "address": ("Warszawa", "Królewska", 15), "gender": True, "age": 39}
p2 = {"name": "Benek", "last_name": "Benkowski", "address": ("Jaroty", "Bartąska", 128), "gender": True, "age": 45}
p3 = {"name": "Andrzej", "last_name": "Spirytus", "address": ("Gdańsk", "Zbójnicka", 2), "gender": True, "age": 35}
p4 = {'name': 'Anna', 'last_name': 'Nowak', 'address': ('Gdynia', 'Morska', 32), 'gender': False, 'age': 27}
p5 = {"name": "Piotr", "last_name": "Sosiński", "address": ("Derc", "Bobrowa", 128), "gender": True, "age": 51}
p6 = {"name": "Jan,", "last_name": "Jankowski", "address": ("Gdańsk", "Towarowa", 38), "gender": True, "age": 30}
p7 = {"name": "Woyt", "last_name": "Brozyna", "adderss": ("Pcim koło warszawki", None, 1), "gender": True, "age": 75}
p8 = {"name": "Katarzyna", "last_name": "Kowalska", "address": ("Gdańsk", "Zbożowa", 4), "gender": True, "age": 40}

users = [p1, p2, p3, p4, p5, p6, p7, p8]

# lista mężczyzn z danego miasta
# SELECT * FROM users WHERE address[1] = ?;


# lista osób z danego przedziału wiekowego
# SELECT * FROM users WHERE age BETWEEN ? AND ?;

# średnia wieku kobiet o imionach rozpoczynających się na A
# SELECT avg(age) FROM users WHERE gender = 0 AND name like 'A%';
