from classes.auto import Auto

auto = Auto("ABC-123", 142)

print(f"""
Auton rekisteritunnus on {auto.rekisteritunnus}
Auton huippunopeus on {auto.huippunopeus}
Auton tämänhetkinen nopeus: {auto.nopeus}
Autolla kuljettu matka: {auto.matka}
""")
