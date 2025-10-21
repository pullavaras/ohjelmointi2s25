from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(70)
auto1.kulje(2)

print(f"""
Rekisteritunnus: {auto1.rekisteristeritunnus}
Huippunopeus: {auto1.huippunopeus}
Nopeus: {auto1.nopeus_nyt}
Matka: {auto1.kuljettu_matka}
      """)


