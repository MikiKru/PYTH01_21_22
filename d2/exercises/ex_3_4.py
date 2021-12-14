import math

x, y = (0, 0)
while True:
    decision = input("kierunek (N/S/E/W) kroki")
    if not decision:
        # dist = math.sqrt(x ** 2 + y ** 2)
        print(f"Robot znalazł się {math.hypot(x, y):.2f} od punktu startowego")
        break
    direction, step = decision.split()
    step = int(step)
    if direction == "N":
        y += step
    elif direction == "S":
        y -= step
    elif direction == "E":
        x += step
    elif direction == "W":
        x -= step
    else:
        print("błędny kierunek")
