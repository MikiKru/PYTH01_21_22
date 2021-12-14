name = "United Nations Educational, Scientific and Cultural Organization"

# wyodrębnij słowa z nazwy
words_clean = name.replace(",", "").split()
print(words_clean)
shortcut = ""
for word in words_clean:
    if word[0].isupper():
        shortcut += word[0]  # shortcut = shortcut + word[0]

print(name, shortcut)
