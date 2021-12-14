record = ('Michał', 'Kruczkowski', 1232324243, True, 12324.32)
print(record)

# pobranie wartości na określonym indeksie
print(record[0])                    # pierwszy
print(record[len(record) - 1])      # ostatni
print(record[-1])                   # ostatni

# niemutowalność !!!
# record[0] = 1       # 'tuple' object does not support item assignment
print(tuple("sdsda"))