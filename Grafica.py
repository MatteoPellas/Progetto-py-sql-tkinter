import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Application(QWidget):
    def __init__(self):
        super().__init__()

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

    def connect(self):
        # Qui andrebbe il codice per connettersi al database utilizzando i valori inseriti dall'utente
        # Ad esempio, si potrebbe utilizzare il modulo mysql.connector per Python

        # Creazione della nuova finestra
        self.new_window = QWidget()
        self.new_window.setWindowTitle('Connected')

        self.label = QLabel('ciao', self.new_window)
        self.label.move(50, 50)

        self.new_window.show()

if __name__ == '__main__':
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
