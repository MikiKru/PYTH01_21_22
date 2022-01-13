import traceback


class MyDigitTypeError(Exception):
    def __init__(self):
        print("Błąd typu cyfr")

while True:
    try:
        number1 = int(input("Podaj pierwszą cyfre parzystą [2-8]"))
        number2 = int(input("Podaj drugą cyfre nieprzystą [1-9]"))
        if (number1 < 0 or number1 > 9) or (number2 < 0 or number2 > 9):
            raise MyDigitTypeError()
        assert number1 % 2 == 0, "pierwsza liczba powinna być parzysta"         # testowanie kodu
        assert number2 % 2 != 0, "druga liczba powinna być nieparzysta"
        print(f"Wynik dzielnia {number1} / {number2} = {number1/number2}")
        break
    except ValueError as e:
        print("Błąd danych")
        print(traceback.format_exc())               # komunikat konsolowy
    except ZeroDivisionError as e:
        print("Błąd dzielenia przez zero")
        print(e)
    except MyDigitTypeError as e:
        print("Musisz podać cyfry w zakresie od 0 do 9")
        print(e)
    except AssertionError as e:
        print("Podane wartości są niezgodne z poleceniami")
    except:
        print("Inny błąd")

print("Mój program dalej działa!")