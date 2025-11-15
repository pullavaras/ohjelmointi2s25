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

autokilpailu = True
while autokilpailu:
    for auto in autot:
        noupeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(noupeuden_muutos)
        auto.kulje(1)
    for auto in autot:
        if auto.matka >= 1000:
            autokilpailu = False

print(f"{'Rekisteritunnus':<10} {'Huippunopeus':<14} {'Nopeus':<8} {'Kuljettu matka':<10}")


for auto in autot:
    print(f"{auto.rekisteritunnus:>10}"
          f"{auto.huippunopeus:>12}"
          f"{auto.nopeus:>14}"
          f"{auto.matka:>10}")