from classes.auto import Auto

auto = Auto("ABC-123", 142)

auto.kiihdytä(50)
auto.kulje(1.5)

print(f"""
Auton rekisteritunnus: {auto.rekisteritunnus}
Auton huippunopeus: {auto.huippunopeus}
Auton tämänhetkinen nopeus: {auto.nopeus}
Autolla kuljettu matka: {auto.matka}
""")
