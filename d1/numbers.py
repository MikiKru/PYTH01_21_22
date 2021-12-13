integer_num = 14
float_num = 1_999_838.32
complex_num = 3 + 3j
print(integer_num)
print(float_num)
print(complex_num)

# systemy pozycyjne
print("decimal", integer_num)
print("binary", bin(integer_num))
print("octal", oct(integer_num))
print("hexadecimal", hex(integer_num))

# operatory
print("power", integer_num ** 2)
print("power", pow(integer_num, 2))     # pow(podstawa, wykładnik)
print("ever or odd", integer_num % 2 == 0)
# 49 % 11 -> ? -> (4 * 11 = 44) -> 49 - 44 = 5
print(49 % 11)
print(7 % 4)

# operacje przypisania
# = vs ==
a = 1            # przypisanie
print(a == 10)   # porównanie zwracające wartość logiczną

a = a * 3        # a += 3
print(a)

binary_from_comm = 0b11010101110
binary_from_comm_clean = str(bin(binary_from_comm)).replace("0b","")
print("Na początku:", binary_from_comm_clean[0])
print("Na końcu:", binary_from_comm_clean[-1])
print("Na końcu:", binary_from_comm_clean[-3 : ])
