# shortcuts
# CTRL + Q              -> docs
# CTRL + /              -> auto-komentarz
# CTRL + D              -> duplikowanie linii
name = 'Python'
print('Hello ' + name)
print('Hello', name, "!")
print(f'Hello {name}! {name} is cool!')          # formatowanie wyjścia

# 1num = 1 - źle
num1 = 1        # ok
num_one = 1     # snake case

if name == 'Python':
    example = "xxxxxxxxxxxxxxxxxxxxxxxxxx" \
              "xxxxxxxxxxxxxx" \
              "xxxxxxxx"
    print(example)
    print("Programujesz w ............................................."
          "...................................Pythonie!")
    print("Super")
else:
    print("Coś innego!")

name = "Michał"
last_name = "Kruczkowski"
status = True
gender = "M"

print(name, last_name, status, gender, sep="; ", end=" ")
print(name, last_name, status, gender, sep="; ", end=" ")
print(name, last_name, status, gender, sep="; ", end=" ")
