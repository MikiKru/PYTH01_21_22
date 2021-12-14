day = int(input("podaj dzień"))
month = int(input("podaj miesiąc"))
year = int(input("podaj rok"))

z = year - 1 if month < 3 else year
c = 0 if month < 3 else 2

day_of_week_index = (int(23 * month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7

print(f"Indeks dnia tygodnia {day_of_week_index}")