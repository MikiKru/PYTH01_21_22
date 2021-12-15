s1 = {1, 2, 3, 4, 5}
s2 = set(range(4, 10))

print(s1)
print(s2)

# dodawanie wartości
s1.add(1)
s1.add(11)
# usuwanie elementu
s2.pop()        # usuwa pierwszy element zbioru
s2.remove(8)    # usuwanie obiektu ze zbioru
print(s1)
print(s2)

print("Suma", s1 | s2, s1, s2)
print("Część wspólna", s1 & s2, s1, s2)
print("Różnica", s1 - s2, s1, s2)
print("Różnica symetryczna", s1 ^ s2, s1, s2)

# sprawdzenie przynależności
print(100 in s1)
print(1 in s1)
print(s1 > {1,2,3})
