# odczyt pliku w1 a po nim w2
with open(r'files\w1.txt', mode="r", encoding='cp1250') as file_w1:
    print(file_w1.read())
    print("==============")
with open(r'files\w2.txt', mode="r", encoding='cp1250') as file_w2:
    print(file_w2.read())
    print("==============")

# odczyt w1 i w2 naprzemiennie linijka po linijce
with open(r'files\w1.txt', mode="r", encoding='cp1250') as w1:
    w1_content = w1.readlines()
with open(r'files\w2.txt', mode="r", encoding='cp1250') as w2:
    w2_content = w2.readlines()

longer_content = w2_content
smaler_content = w1_content
if len(w1_content) > len(w2_content):
    longer_content = w1_content
    smaler_content = w2_content

for index, content in enumerate(longer_content):
    print(longer_content[index].strip())
    if len(smaler_content) > index:
        print(smaler_content[index].strip())