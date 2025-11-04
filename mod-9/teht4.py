from classes.auto import Auto
import random

autot = []

for a in range(1,11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" +str(a), huippunopeus))

kokonaismatka = 0
while kokonaismatka < 10000:
    for auto in autot:
        auton_nopeus = random.randint(-10, 15)
        auto.kiihdytä(auton_nopeus)
        auto.kulje(1)
        if auto.matka > kokonaismatka:
            kokonaismatka = auto.matka

for auto in autot:
    print(f"{auto.rekisteritunnus:<8} {auto.huippunopeus:>8} {auto.nopeus:>8} {auto.matka:>10}")
