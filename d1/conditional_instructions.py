# name = input("podaj imię: ")

# if name[-1] == 'a':
#     print('Imię żeńskie')
# else:
#     print('Imię męskie')

print("Imię żeńskie" if input("podaj imię: ")[-1] == 'a' else 'Imię męskie')

number = 0

if number == 0:
    print("liczba zero")
elif number > 0 and number % 2 == 0:
    print("liczba dodatnia parzysta")
elif number < 0 and number % 2 == 0:
    print("liczba ujemna parzysta")
elif number > 0 and number % 2 != 0:
    print("liczba dodatnia nieparzysta")
else:
    print("liczba ujemna nieparzysta")