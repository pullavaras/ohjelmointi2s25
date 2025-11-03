from classes.auto import Auto

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"""
Auton rekisteritunnus: {auto.rekisteritunnus}
Auton huippunopeus: {auto.huippunopeus}
Auton tämänhetkinen nopeus: {auto.nopeus}
Autolla kuljettu matka: {auto.matka}
""")

auto.kiihdytä(-200)

print(f"""
Auton rekisteritunnus: {auto.rekisteritunnus}
Auton huippunopeus: {auto.huippunopeus}
Auton tämänhetkinen nopeus: {auto.nopeus}
Autolla kuljettu matka: {auto.matka}
""")
