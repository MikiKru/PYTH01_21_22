def day_index(date: str, sep: str = "-") -> int:
    z: int
    c: int
    year, month, day = date.split(sep)
    year = int(year)
    month = int(month)
    day = int(day)
    z = year - 1 if month < 3 else year
    c = 0 if month < 3 else 2
    return (int(23 * month / 9) + day + 4 + year + (z // 4) - (z // 100) + (z // 400) - c) % 7


def day_name(day_index: int) -> str:
    day_name_mapper: tuple
    day_name_mapper = ('niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota')
    return day_name_mapper[day_index]


def get_day_name() -> None:
    sep: str
    date: str
    while True:
        sep = input("wybierz separator \"-\" lub \".\"")
        if sep != "-" and sep != ".":
            continue
        date = input("podaj datę zgodnie z wybranym separatorem: ")
        if date[4] != "-" and date[2] != ".":
            continue
        print(f"Dzień dla podanej daty {date} to {day_name(day_index(date, sep))}")
        break


# day_index(1, "-")     - błąd typu w argumencie
# day_name("XXX")       - błąd typu w argumencie
# x = get_day_name()    - błąd typu zwracanej wartości
get_day_name()
