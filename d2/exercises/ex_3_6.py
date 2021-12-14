import re

text = "kajak"
# oczyść tekst -> zostają tylko znaki alfanumeryczne i podniesione do wielkich liter
clean = ''.join(c.upper() for c in text if c.isalnum())
# print(re.findall('[a-zA-z]+',text.upper()))
# for c in text:
#     if c.isalnum():
#         clean += c.upper()
half_len = len(clean) // 2
print(clean[0:half_len], clean[-1: -(half_len+1):-1])
