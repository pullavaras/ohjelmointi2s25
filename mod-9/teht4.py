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

for a in range(1, 11):
    rekisteritunnus = "ABC-" + str(a)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

while True:
    noupeuden_muutos = random.randint(-10, 15)
    auto.kiihdytä(noupeuden_muutos)

    for auto in autot:
        auto.kulje(1)