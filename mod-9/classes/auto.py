class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    
    def kiihdytä(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        return

        
        # lisää muutos self nopeuteen
        # tarkasta ettei nopeus ole yli huippunopeuden
        # jos on, aseta nopeus = huippunopeus
        # tarkasta ettei nopeus ole alle nolla
        # jos on, aseta nopeus = 0

