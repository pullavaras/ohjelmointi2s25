import random

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, kmh):
        self.nopeus += kmh
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        kuljettu = self.nopeus * tunnit
        self.matka += kuljettu


autot = []

for a in range(10):
    autot.append("ABC-"+str(a+1))
print(autot)

huippunopeus = random.randint(100, 200)
