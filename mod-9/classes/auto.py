class Auto:
    def __init__(self, uusi_rekisteritunnus, uusi_huippunopeus):
        self.rekisteristeritunnus = uusi_rekisteritunnus
        self.huippunopeus = uusi_huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0