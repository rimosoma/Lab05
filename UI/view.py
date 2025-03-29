import flet as ft
from UI.controller import Controller


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements

        self._title = None

        self.row1 = None
        self._tendina = None
        self.btn_cercaIscritti = None

        self.row2 = None
        self.matricola = None
        self.nomeStud = None
        self.cognomeStud = None
        self.btn_cercaStudente = None

        self.row3 = None
        self.btn_cercaCorsi = None


        self.console = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self.row1 = ft.Row(spacing=30, controls=[self._title ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(self.row1)
        self._page.update()

        #ROW with dropdown and button
        self._tendina = ft.Dropdown(label="Opzioni", hint_text="Seleziona Corso", on_change=self.controller.setCorso )
        opzioni = self.controller.getOpzioniTendina()
        for tupla in opzioni:
            self._tendina.options.append(ft.dropdown.Option(key= tupla[0], text= tupla[1]))
        self._page.update()

        # button for the "hello" reply
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_CercaIscritti)
        row1 = ft.Row([self._tendina, self.btn_cercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.update()



        self.matricola = ft.TextField(label="matricola senza s", on_change=self.controller.setMatricola)
        self.nomeStud = ft.TextField(label="Nome Studente",read_only=True )
        self.cognomeStud= ft.TextField(label="Cognome Studente",read_only=True )
        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_CercaStudente)
        self.row2 = ft.Row(spacing=30, controls=[self.matricola, self.nomeStud,self.cognomeStud, self.btn_cercaStudente ], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(self.row2)

        self._page.update()


        self.btn_cercaCorsi = ft.ElevatedButton(text="Corsi a cui è iscritto",visible=False , on_click=self._controller.handle_cercaCorsiStud)
        self.row3 = ft.Row(spacing=30, controls=[self.btn_cercaCorsi], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(self.row3)


        # List View where the reply is printed
        self.console = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.console)
        self._page.update()





    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
