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

    def kulje(self, tunnit):
        #self.matka = 2000
        #self.nopeus = 60
        self.matka = self.matka + self.nopeus * tunnit
        return
