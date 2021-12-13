values = [1,2,3,2,1,4,5,4,3,6,5]
to_find = 20

# for objekt_pomocniczy in sekwencja:
for value in values:
    print(value)
    if value != to_find:
        continue        # przechodzę do kolejnen iteracji
    print(f"Wartość {to_find} znajduje się na naszej liście")
    break               # przerywa działąnie pętli - wychodzi z pętli
else:                   # else się wykona gdy pętla zakończy dizałanie w sposób naturalny bez przerwania
    print(f"Nie zanleziono oczekiwanej wartości {to_find}")


for character in "ABCDEFGH":
    print(character)

