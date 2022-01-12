import d4.ex_5_5.ex_5_5 as mod  # 'wklejam' kod znajdujący się w module ex_5_5
import math                     # 'wklejam' cały kod z biblioteki math

from datetime import date       # importuję tylko jedną składową z modułu datetime
from datetime import time as t

import requests
from numpy import max, array

user_from_module = mod.User("Michał", "Kot", True, 2000)
print(user_from_module)
print(math.e)               # muszę dodawać na początku nazwę modułu

print(date.today())         # nie dodaję nazwy modułu
print(t.min)

# w terminalu pip install requests -> instaluje w środowisku wirtualnym zestaw bibliotek requests
page = requests.get("https://www.wp.pl/")
# print(page.content)

print(max(array([1,2,3,4,3,2])))

