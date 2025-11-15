from classes.auto import Auto
import random

class Kilpailu:

    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            noupeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(noupeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteritunnus':<10} {'Huippunopeus':<14} {'Nopeus':<8} {'Kuljettu matka':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:>10}"
                  f"{auto.huippunopeus:>12}"
                  f"{auto.nopeus:>14}"
                  f"{auto.matka:>10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False
