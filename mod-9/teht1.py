from classes.auto import Auto

auto1 = Auto("ABC-123", 142)

print(f"""
    Rekisteritunnus: {auto1.rekisteritunnus}
    Huippunopeus: {auto1.huippunopeus}
    Tämänhetkinen nopeus: {auto1.nopeus}
    Kuljettu matka: {auto1.matka}
    """)