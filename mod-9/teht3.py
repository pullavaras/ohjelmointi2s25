from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
print(f"""
    Auto 1
    Rekisteritunnus: {auto1.rekisteritunnus}
    Huippunopeus: {auto1.huippunopeus}
    Tämänhetkinen nopeus: {auto1.nopeus}
    Kuljettu matka: {auto1.matka}
    """)

auto1.kulje(3)
print(f"""
    Auto 1
    Rekisteritunnus: {auto1.rekisteritunnus}
    Huippunopeus: {auto1.huippunopeus}
    Tämänhetkinen nopeus: {auto1.nopeus}
    Kuljettu matka: {auto1.matka}
    """)