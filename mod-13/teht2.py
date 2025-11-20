import mysql.connctor
from flask import Flask, Response
import json

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='linneag',
    password='3852335587',
    autocommit=True
    )

def haku(icao):
    sql = f'SELECT name, municipality FROM airport where ident = "{icao}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

