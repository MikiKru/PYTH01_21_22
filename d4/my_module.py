global_value = 5

def power(x, y):
    result = 1
    while(y):
        result *= x
        y -= 1
    return result

class Auto:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.equipment = []
    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.equipment}"