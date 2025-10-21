class Auto:

    def __init__(self, uusi_rekisteritunnus, uusi_huippunopeus):
        self.rekisteristeritunnus = uusi_rekisteritunnus
        self.huippunopeus = uusi_huippunopeus
        self.nopeus_nyt = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, arvo):
        pass
        # lisää arvo sefl nopeuteen
        # tarkasta ettei nopeus ole yli huippunopeuden
        # jos on, aseta nopeus = huippunopeus
        # tarkasta ettei nopeus ole alle nolla
        # jos on, aseta nopeus = 0

    def kulje(self, aika):
        pass
        # laske kuinka palon auto on kulkenut annetussa ajassa tietyllänopeudella
        # lisää kuljettu matka kokonaismatkaan
#