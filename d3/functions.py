from random import random

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


