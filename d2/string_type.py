import re

name = "Michał"

# Michał
# 01234----> długość napisu - 1

# pobranie wartości znajdującej się na indeksie
print(name[0])
print(name[1])

# zabronione - typ niemutowalny!
# name[0] = 'K'       # 'str' object does not support item assignment

# backslesh \ działa jak znak specjalny
quote = "My favourite quote: \"I\'m your father!\""
print(quote)
url = "xyz.pl\\new"
print(url)
print('abnormal', 'a\bnormal')

# tablica ASCII
print(ord("M"), ord("i"), ord("c"))
print(chr(77), chr(105), chr(99))
# porównanie napisów
print("Ala" > "Ola")
print("Alaaaaaaa" > "Alan")  # leksykograficznie - indeks po indeksie
print("Ala" == "ala")

# replace
tab = chr(9)
cr = chr(10)
print(tab, cr)
read = "dskadop" + tab + "das" + tab + "das" + cr + "sdad" + tab + cr
print(read.replace(chr(9), "").replace(chr(10), ""))
clean = ""
for c in read:
    if c.isalnum():
        clean += c
print(clean)
read2 = "   abc    sda   sd          "
print(read2.strip())  # usunięcie znaków białych początek i koniec
# regexp_replace('tekst',,''')
print(re.sub('\s{2,}', ' ', read2).strip())

name = "Michał"
name1 = "Aleksandra"
staus = True
number = 123.3281
print(f"|{name:>20}|{staus:10}|{number:20.2f}|")
print(f"|{name1:>20}|{staus:10}|{number:20.2f}|")
print(f"|{name:>20}|{staus:10}|{number:20.2f}|")
print(f"|{name:>20}|{staus:10}|{number:20.2f}|")

# metody dla stringa
text = "Ala ma kota a kot ma  Ale"
print(text.zfill(10))
print(text.find("kot"))

print(text, text.split(" "))
new_text = text + " inny tekst"
print(new_text)