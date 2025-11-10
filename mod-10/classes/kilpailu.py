

class Kilpailu:

    def __init__(self, nimi, km, autolista):
        self.nimi = nimi
        self.km = km
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
