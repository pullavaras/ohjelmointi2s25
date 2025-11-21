import mysql.connector
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/kentta/<icao>')
def haku(icao):
    try:
        yhteys = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='flight_game',
            user='linneag',
            password='3852335587',
            autocommit=True
        )

        sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}"'
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()

        if tulos:
            tilakoodi = 200
            vastaus = {
                "ICAO": icao,
                "Name": tulos[0],
                "Municipality": tulos[1]
            }
        else:
            tilakoodi = 404
            vastaus = {
                "status": tilakoodi,
                "teksti": "ICAO-koodia ei löytynyt."
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen ICAO-koodi."
        }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhe):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
