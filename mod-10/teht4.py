from classes.kilpailu import Kilpailu
from classes.auto import Auto
import random

autot = []
for a in range(1, 11):
    rekisteritunnus = "ABC-" + str(a)
    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

romuralli = Kilpailu("Suuri Romuralli", 8000, autot)

tunnit = 0
while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"\nKilpailun tilanne {tunnit}. tunnin jälkeen:")
        romuralli.tulosta_tilanne()

print("\nKilpailu on päättynyt! Lopputilanne:")
romuralli.tulosta_tilanne()

