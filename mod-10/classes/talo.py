from .hissi import Hissi

class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissit_kpl):
        self.hissit = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit_kpl = hissit_kpl

        for i in range(hissit_kpl):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissi_nro, kerros):
        print(f"Olet hississä {hissi_nro}")
        hissi = self.hissit[hissi_nro]
        hissi.siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("Talossa on palohälytys. Kaikki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)
