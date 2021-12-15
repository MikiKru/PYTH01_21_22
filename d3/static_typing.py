# opis funkcji w komentarzu jest dostępny dla programisty - dostępny w źródłach
def addition(x: float, y: float) -> float:
    """
    Funkcja do obliczania sumy dwóch skłądników.

    :param x: skłądnik pierwszy
    :param y: składnik drugi
    :return: suma
    """
    return x + y


print(addition(1, 1))
print(addition("1", "1"))       # typowanie statyczne pomaga rozpoznać sytuację wyjątkowe na wczesnym etapie implementacji

help(addition)
print(addition.__doc__)
