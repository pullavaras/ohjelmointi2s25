from classes.auto import Auto

class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akku_kwh):
        Auto.__init__(self, rekisteritunnus, huippunopeus)
        self.akku_kwh = akku_kwh

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankki_l):
        self.bensantankki_l = bensatankki_l
        Auto.__init__(self, rekisteritunnus, huippunopeus)

sähköauto = Sähköauto("ABC-15", 164, 52.5)
sähköauto.kiihdytä(120)
sähköauto.kulje(4)


polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)
polttomoottoriauto.kiihdytä(130)
polttomoottoriauto.kulje(2.2)


print(f"Sähköautolla kuljettu matka: {sähköauto.matka}")
print(f"Polttomoottoriautolla kuljettu matka: {polttomoottoriauto.matka}")