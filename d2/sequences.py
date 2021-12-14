numbers = range(-30, 31)

print(*numbers)
print("parzyste: ", *numbers[::2])
print("parzyste odwrócona kolejność: ", *numbers[::-2])
print("pierwsze 10 liczb: ", *numbers[:11])

# wydobycie elemntów składowych z daty
date = "2000-02-01"
year, month, day = date.split("-")
print(year, month, day)

data = "FF0234032FF"
flag0, flag1, *content, crc0, crc1 = data
print(flag0, flag1)
print(content)
print(crc0, crc1)