day = int(input("podaj dzień: "))
month = int(input("podaj miesiąc: "))
year = int(input("podaj rok: "))

z = year - 1 if month < 3 else year
c = 0 if month < 3 else 2
# // dzielenie podłogowe

day_index = (int(23*month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7
day_name = ('niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota')
print(day_index, day_name[day_index])