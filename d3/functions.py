from random import random
from statistics import mean

def hello():
    print("hello world!".upper())
def hello_me(name):
    print(f"hello {name}".upper())
def division(x, y):
    if y == 0:
        return 'Błąd dzielenia przez zero!'
    return x / y
def get_normalized_random():
    return f"Wylosowana wartość: {random()}"
def get_unique_value_upper_tresh(values, treshold = 0):
    return set([v for v in values if v >= treshold])
def get_avg_from_grades(*grades):
    print(grades)       # krotka
    return mean(grades)
def get_avg_from_grades_named(**grades):
    print(grades)       # słownik
    return mean(grades.values())