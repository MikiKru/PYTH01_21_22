class Address:
    def __init__(self, street, post_code, city):
        self.street = street
        self.post_code = post_code
        self.city = city
    def to_csv(self):
        return f"{self.street};{self.post_code};{self.city}"
    def __str__(self):
        return f"{self.street} {self.post_code} {self.city}"
