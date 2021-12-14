year = int(input("podaj rok: "))
day = 13
friday_13_counter = 0

for month in range(1, 13):
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    day_index = (int(23*month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7
    if day_index == 5:      # piątek 13-ego
        friday_13_counter += 1

print(f"Liczba piątków 13-ego w roku {year} to {friday_13_counter}")

# ile piątków 13 w okresie x ostatnich lat
friday_13_counter_global = 0
for year in range(2001, 2022):
    friday_13_counter = 0
    for month in range(1, 13):
        z = year - 1 if month < 3 else year
        c = 0 if month < 3 else 2
        day_index = (int(23*month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7
        if day_index == 5:      # piątek 13-ego
            friday_13_counter += 1
            friday_13_counter_global += 1
    print(f"Liczba piątków 13-ego w roku {year} to {friday_13_counter}")

print("Sumaryczna ilość piątków 13-ego", friday_13_counter_global)