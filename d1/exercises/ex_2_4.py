import math

n = 49
k = 6

combs = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

print(f"Ilość kombinacji: {combs}")
print(f"Szanse na trafienie: {1/combs:.10f}")