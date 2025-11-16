import json
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyyntö).json()

print("Satunnainen Chuck Norris- vitsi:")
print(vastaus["value"])

