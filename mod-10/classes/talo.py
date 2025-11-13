from .hissi import Hissi

class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissit_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

        self.hissit = []
        for h in range(hissit_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissiä(self, hissin_nro, kohde_krs):
        hissi = self.hissit[hissin_nro - 1]
        print("Ajat hissiä", hissin_nro)
        hissi.siirry_kerrokseen(kohde_krs)

    def palohälytys(self):
        print("Palohälytys! Kaiki hissit siirtyvät pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)
