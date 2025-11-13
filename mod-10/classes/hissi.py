class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerroksessa = alin_kerros

    def kerros_alas(self):
        self.kerroksessa -= 1
        print(f"Olet {self.kerroksessa}. kerroksessa.")

    def kerros_ylös(self):
        self.kerroksessa += 1
        print(f"Olet {self.kerroksessa}. kerroksessa.")

    def siirry_kerrokseen(self, kerros):
        if kerros < self.alin_kerros or kerros > self.ylin_kerros:
            print("Virheellinen kerros.")
            return

        while self.kerroksessa != kerros:
            if kerros > self.kerroksessa:
                self.kerros_ylös()
            elif kerros < self.kerroksessa:
                self.kerros_alas()

