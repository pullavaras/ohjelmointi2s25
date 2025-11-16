import json
import requests

paikka = input("Anna paikkakunta, ja saat säätiedot: ")
apiavain = "###"
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid={apiavain}&units=metric&lang=fi"

try:

    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()

        kaupunki = json_vastaus['name']
        sää = json_vastaus['weather'][0]['description']
        lämpötila = json_vastaus['main']['temp']

        print(f"Sää paikassa {kaupunki} on {sää}.")
        print(f"Lämpötila on {lämpötila:.1f} astetta C.")

    else:
        print("Haku epäonnistui.")

except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")
