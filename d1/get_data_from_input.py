# - komentarz
# name = input("podaj imię ")
# print(f"Hello {name.upper()}")

x = 1
y = x
print(x, y)
x = 2       # obiekty - zmienne przekaywane są przez wartość
print(x, y)
print(id(x), id(y))
float_number = 1.83

print(type(x), type(float_number), type("XYZ"), type(True))
# konwersja - zawężająca
print(int(float_number), round(float_number, 0))
# konwersja rozszerzająca
print(float(x))

