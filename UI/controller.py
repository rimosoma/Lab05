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
        self._view.btn_cercaCorsi.visible = False
        self._view.btn_cercaCorsi.update()
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
            alert = ft.AlertDialog(title=ft.Text("Inserire un corso"))
            self._view._page.dialog = alert  # Assegna il dialog alla pagina
            alert.open = True  # Imposta il flag di apertura
            self._view._page.update()  # Aggiorna la UI per renderlo visibile            return []


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
                    alert = ft.AlertDialog(title=ft.Text("Inserire una matricola"))
                    self._view._page.dialog = alert  # Assegna il dialog alla pagina
                    alert.open = True  # Imposta il flag di apertura
                    self._view._page.update()  # Aggiorna la UI per renderlo visibile
            except KeyError or ValueError:
                self._view.console.clean()
                print(self.matrStudInteresse)
                self._view.console.controls.append(ft.Text("la matricola non esiste", color="red"))
                self._view._page.update()
        else:
            alert = ft.AlertDialog(title=ft.Text("Inserire una matricola"))
            self._view._page.dialog = alert  # Assegna il dialog alla pagina
            alert.open = True  # Imposta il flag di apertura
            self._view._page.update()  # Aggiorna la UI per renderlo visibile


    def setCorso(self, e):
        self.codCorsoInteresse =  e.control.value

    def setMatricola(self,e ):
        if e.control.value.strip()== "":
            self.matrStudInteresse = ""
            self._view.nomeStud.value = ""
            self._view.cognomeStud.value = ""
            self._view._page.update()
        try:

            self.matrStudInteresse =  int(e.control.value)
            self._view.console.clean()
            self._view._page.update()
        except ValueError:
            self._view.console.clean()
            self._view.console.controls.append(ft.Text("inserire matricola in numeri", color="purple"))
            self._view._page.update()
