# record = {1 : ("M","K","2000-02-02",True, 10000.5)}
# record = {1 : user}

roman_to_arabic = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}

for key, value in roman_to_arabic.items():
    print(key, value)

print({ key : value for key, value in roman_to_arabic.items() })
arabic_to_roman = { value : key for key, value in roman_to_arabic.items() }
print(arabic_to_roman)

# pobieranie wartości po kluczu
print(roman_to_arabic["I"])
print(arabic_to_roman[4])

# dodawanie nowych elementów
roman_to_arabic["VI"] = 6
print(roman_to_arabic)

# wyszukiwanie kluczy
rta_keys = roman_to_arabic.keys()
print(1 in rta_keys)
print("I" in rta_keys)

# aktualizowanie wartości
roman_to_arabic["V"] = 6
print(roman_to_arabic)

