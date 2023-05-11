import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from Wrapper import Wrapper


class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.new_window = None
        self.w: Wrapper = Wrapper()
        self.w.creaDipendente()
        self.w.creaMansione()
        self.w.creaReparto()

        # Creazione dei campi di input
        self.server_label = QLabel('Server')
        self.server_input = QLineEdit()

        self.username_label = QLabel('Username')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Password')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.database_label = QLabel('Nome Database')
        self.database_input = QLineEdit()

        # Creazione del pulsante di connessione
        self.connect_button = QPushButton('Connect')
        self.connect_button.clicked.connect(self.connect)

        # Creazione della layout verticale
        layout = QVBoxLayout()
        layout.addWidget(self.server_label)
        layout.addWidget(self.server_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.database_label)
        layout.addWidget(self.database_input)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)
        self.setWindowTitle('Application')

    def b1f(self):
        print("b1f works")

    def b2f(self):
        print("b2f works")

    def b3f(self):
        print("b3f works")

    def b4f(self):
        print("b4f works")

    def b5f(self):
        print("b5f works")

    def b6f(self):
        print("b6f works")

    def b7f(self):
        print("b7f works")

    def connect(self):
        # Qui andrebbe il codice per connettersi al database utilizzando i valori inseriti dall'utente
        # Ad esempio, si potrebbe utilizzare il modulo mysql.connector per Python

        # Creazione della nuova finestra
        self.new_window = QWidget()
        self.new_window.setWindowTitle('Connected')

        self.b1 = QPushButton('Inserisci Mansione')
        self.b2 = QPushButton('Inserisci Reparto')
        self.b3 = QPushButton('Inserisci Dipendenti')
        self.b4 = QPushButton('Visualizza')
        self.b5 = QPushButton('Calcolo dello stipendio medio')
        self.b6 = QPushButton('Elenco dei dipendenti')
        self.b7 = QPushButton('Calcolo dello stipendio minimo')

        layout = QVBoxLayout()
        print("alksdj")
        for i, j in zip([self.b1,  self.b2,  self.b3,  self.b4,  self.b5,  self.b6,  self.b7],
                        [self.b1f, self.b2f, self.b3f, self.b4f, self.b5f, self.b6f, self.b7f]):
            i.clicked.connect(j)
            layout.addWidget(i)
            """
            layout.addWidget({ i.clicked.connect(j); i });
            """

        self.new_window.setLayout(layout)

        self.new_window.show()


if __name__ == '__main__':
    # Cose di pyqt5
    app = QApplication(sys.argv)
    login = Application()
    login.show()
    sys.exit(app.exec_())

"""
Calcolo dello stipendio medio dei dipendenti raggruppati per città
b. Elenco dei dipendenti che sono nati nel mese di aprile, maggio e giugno(valori
inseriti anche da input)
c. Calcolo dello stipendio minimo e massimo per ciascun reparto
"""
