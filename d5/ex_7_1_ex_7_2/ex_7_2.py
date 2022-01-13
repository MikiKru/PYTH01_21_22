# zapis do pliku zawartości obu plików w1 i w2

with open(r'files\w3.txt', mode="w", encoding='cp1250') as file_w3:
    with open(r'files\w1.txt', mode="r", encoding='cp1250') as file_w1:
        file_w3.write(file_w1.read() + "\n\n")
    with open(r'files\w2.txt', mode="r", encoding='cp1250') as file_w2:
        file_w3.write(file_w2.read())
