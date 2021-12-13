decision = True

print(decision)
print(bool(0), bool(0.0), bool(None), bool(""), bool([]), bool({}))
name = "Michał"

if decision or not name == "Adam":
    print("Warunek prawdziwy")