year = int(input("podaj rok"))

is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(f"Rok {year} jest przestępny: {is_leap}")