import flet as ft
from UI import view
from model.studente import Studente
from model.corso import Corso
from database.corso_DAO import corsoDAO
from database.studente_DAO import studenteDAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._corsoDao = corsoDAO()
        self._studenteDAO = studenteDAO()

        self.codCorsoInteresse = None
        self.matrStudInteresse = None


    def getOpzioniTendina(self):
        dizionario = self._corsoDao.getAllCorsi()
        listaTuple = []
        for chiave, Corso in dizionario.items():
            tupla = (chiave, Corso.nome)
            listaTuple.append(tupla)
        #print((listaTuple[0])[0])
        return listaTuple




    def handle_cercaCorsiStud(self, e):

        DictCodCorsi = self._studenteDAO.getCorsiStudente(self.matrStudInteresse)
        listaTuple = []
        self._view.console.clean()
        self._view.console.controls.append(ft.Text("Corsi frequentati: "))
        for codcorso, Corso in DictCodCorsi.items():
            tupla = (codcorso, Corso.nome)
            listaTuple.append(tupla)
            self._view.console.controls.append(ft.Text(tupla))
        self._view._page.update()

        return listaTuple



    def handle_CercaIscritti(self, e):
        """  """
        if self.codCorsoInteresse:
            DictmatricolaStudente = self._corsoDao.getStudentiCorso(self.codCorsoInteresse)
            listaTuple = []
            self._view.console.clean()
            self._view.console.controls.append(ft.Text("Iscritti al corso: "))
            for matricola, Studente in DictmatricolaStudente.items():
                tupla = (matricola, (Studente.nome +","+ Studente.cognome))
                listaTuple.append(tupla)
                self._view.console.controls.append(ft.Text(tupla))
            self._view._page.update()
            return listaTuple
        else:
            print("non è stato assegnato il corso di interesse")
            return []


    def handle_CercaStudente(self, e):
        if self.matrStudInteresse:
            try:
                #print(self._studenteDAO.getAllStudenti()[154817])
                #print(self.matrStudInteresse)
                studenteCercato = self._studenteDAO.getAllStudenti()[self.matrStudInteresse]
                if studenteCercato:
                    self._view.nomeStud.value = studenteCercato.nome
                    self._view.cognomeStud.value = studenteCercato.cognome
                    self._view.btn_cercaCorsi.visible = True
                    self._view.btn_cercaCorsi.update()
                    self._view._page.update()
                    return studenteCercato
                else:
                    print("lo studente non esiste")
            except KeyError:
                print("il studente non esiste")
        else:
            print("inserire matricola")


    def setCorso(self, e):
        self.codCorsoInteresse =  e.control.value

    def setMatricola(self,e ):
        self.matrStudInteresse =  int(e.control.value)

