class PrepaidPhoneError(Exception):
    def __init__(self):
        print("Brakuje środków na rozmowę. Zostanie pobrane z Twojej karty 100zł")

class PrepaidPhone:
    def __init__(self, limit):
        self.__limit = limit
    def get_limit(self):
        return self.__limit
    def add_to_limit(self, value):
        self.__limit += value
    def call(self, call_time):
        print("rozmowa rozpoczęta!")
        try:
            if call_time > self.__limit:
                raise PrepaidPhoneError()
            self.__limit -= call_time
            print("rozmowa zakończona!")
            print("aktualny stan konta:", self.__limit)
        except PrepaidPhoneError:
            self.add_to_limit(100)

pp = PrepaidPhone(150)
pp.call(50)
pp.call(70)
pp.call(50)
pp.call(50)