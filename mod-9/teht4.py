from classes.auto import Auto

autot = []

for i in range (1, 11):
    # arvo huippunopeus 100-200
    huippunopeus = 0
    autot.append(Auto("ABC" + str(i), huippunopeus))

kokonaismatka = 0
while kokonaismatka < 10000:
    for auto in autot:
        #arvo nopeuden muutos 10 - 15
        # kutsu kiihdytä
        auto.kulje(1)

    # toinen silmukka, jossa käydään autot läpi
        # haetaan matkan arvo, jos yli 10000, lopeta kisa asettamalla auton matka kokonaismatkaksi

# etsi joku taulukkokirja tulostamiseen#