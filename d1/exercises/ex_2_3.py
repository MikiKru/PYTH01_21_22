value = 100_000
percent = .54
time = 3

final_value = value * (1 + (percent/100)) ** time

print(f"Kwota po upływie {time} lat to {final_value:.2f} zł")