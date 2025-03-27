# Add whatever it is needed to interface with the DB Table studente
from model.studente import Studente
from model.corso import Corso
from database.DB_connect import get_connection

class corso_DAO:
    def __init__(self):
        self.mappaStudenti = self.getAllStudenti()


    def getAllStudenti(self):
        # cnx = mysql.connector.connect(
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select * from studente s"""
        cursor.execute(query)
        rows = cursor.fetchall()
        res = {}

        for row in rows:
            # codice = row["codins"] #str
            # cognome = row["cognome"] #int
            # nome = row["nome"] #str
            # cds = row["CDS"] #int
            res[row["matricola"]] = (Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cnx.close()

        return res

    def getCorsiStudente(self, matricola):

        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.codins, c.crediti, c.nome, c.pd
FROM studente s
JOIN iscrizione i ON s.matricola = i.matricola
JOIN corso c ON i.codins = c.codins
WHERE s.matricola = %s ;"""

        cursor.execute(query, matricola)

        rows = cursor.fetchall()
        res = {}
        for row in rows:
            res[row["codins"]] = (Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
            cnx.close()

            return res


