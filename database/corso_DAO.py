
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente

import mysql.connector

class corsoDAO:
    def __init__(self):
        self.mappaCorsi = self.getAllCorsi()



    def getAllCorsi(self):
        # cnx = mysql.connector.connect(
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * from corso c"""
        cursor.execute(query)
        rows = cursor.fetchall()
        res = {}

        for row in rows:
            # codice = row["codins"] #str
            # crediti = row["crediti"] #int
            # nome = row["nome"] #str
            # periodo = row["pd"] #int
                res[row["codins"]] = (Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cnx.close()

        return res


    def getStudentiCorso(self, codins):
        #print(codins)
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.matricola, s.cognome, s.nome, s.CDS
FROM corso c
JOIN iscrizione i ON c.codins = i.codins
JOIN studente s ON i.matricola = s.matricola
WHERE c.codins = %s ;"""

        cursor.execute(query, (codins,))

        rows = cursor.fetchall()
        res = {}
        for row in rows:
            res[row["matricola"]] = (Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cnx.close()

        return res




















    """

    def getAllIscrizioni(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "select * from iscrizione i"
        cursor.execute(query)
        rows = cursor.fetchall()
        res = []

        for row in rows:
            # matricola = row["codins"] #str
            # codins = row["codins"] #int

            res.append([row["matricola"], row["codins"]])
        cnx.close()

        return res

"""