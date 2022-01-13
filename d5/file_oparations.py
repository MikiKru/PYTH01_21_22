# bez managera konekstu
import io

f1 = open("example.txt", mode='w', encoding='utf-8')      # otwarcie strumienia
# operacje
print(f1.encoding, f1.mode, f1.closed, f1.name)
f1.write("zawartość pliku")
f1.close()                              # zamknięcie strumienia

# z wykorzystaniem managera konekstu i ścieżki bezpośredniej
text = ["pierwsza\n", "druga\n", "trzecia\n"]
with open(r'C:\Users\pc\Desktop\example1.txt', mode="w", encoding='utf-8') as file1:
    file1.writelines(text)

# z wykorzystaniem managera kontekstu i ścieżki pośredniej
with open(r'files\csv\example2.csv', mode="a", encoding='cp1250') as file2:
    file2.write("dodaje kolejną linijkę do pliku\n")

# odczyt z wykorzystaniem managera konekstu
with open(r'files\csv\example2.csv', mode="r", encoding='cp1250') as file3:
    print(file3.read())
    print("==============")
    file3.seek(0)           # przesuwa na początek pliku gdy 0 a na koniec gdy -1
    print(file3.readlines())
    print("==============")
    file3.seek(0)           # przesuwa na początek pliku gdy 0 a na koniec gdy -1
    for line in file3.readlines():
        print(line.strip())
