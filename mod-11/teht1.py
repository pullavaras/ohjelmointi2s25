class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu: {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivum):
        self.kirjoittaja = kirjoittaja
        self.sivum = sivum
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija on {self.kirjoittaja} ja sivumäärä on {self.sivum}.\n")


class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittjaja):
        self.päätoimittaja = päätoimittjaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja on {self.päätoimittaja}.")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()
lehti.tulosta_tiedot()

