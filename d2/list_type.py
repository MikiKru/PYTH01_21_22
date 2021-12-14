# ctrl + alt + L -> auto-formatowanie

numbers = [3, 2, 1, 4, 2, 3, 2, 3, 4]
print(numbers)
# odwołanie do elementów listy
print(numbers[0])
print(numbers[-1])
# modyfikacja elementów
numbers[0] = 123
print(numbers)
# usuwanie elementów
numbers.remove(numbers[0])  # usuwam pierwszy element z listy
numbers.remove(numbers[2])
print(numbers)
# wstawianie elementów pomiędzy wartości istniejące
numbers.insert(3, None)
numbers.insert(3, "")
print(numbers)
