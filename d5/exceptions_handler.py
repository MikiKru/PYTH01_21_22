import traceback


class MyDigitTypeError(Exception):
    def __init__(self):
        print("Błąd typu cyfr")

while True:
    try:
        number1 = int(input("Podaj pierwszą cyfre [0-9]"))
        number2 = int(input("Podaj drugą cyfre [0-9]"))
        if (number1 < 0 or number1 > 9) or (number2 < 0 or number2 > 9):
            raise MyDigitTypeError()
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
    except:
        print("Inny błąd")

print("Mój program dalej działa!")