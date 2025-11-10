class Hissi:
    
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f"Hissi on nyt {self.nykyinen_kerros} kerroksessa.")
        
    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f"Hissi on nyt {self.nykyinen_kerros} kerroksessa.")

    def siirry_kerrokseen(self, kerrokseen):
        if kerrokseen < self.alin_kerros or kerrokseen > self.ylin_kerros:
            print("Virheellinen kerros.")
            return
        while self.nykyinen_kerros < kerrokseen:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerrokseen:
            self.kerros_alas()



