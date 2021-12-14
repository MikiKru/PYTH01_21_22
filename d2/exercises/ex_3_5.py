name = "United Nations Educational, Scientific and Cultural Organization"

print(name, "".join(word[0] for word in name.replace(",", "").split() if word[0].isupper()))
