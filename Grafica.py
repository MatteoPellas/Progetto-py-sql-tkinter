import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout

from Wrapper import Wrapper


class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.new_window1 = None
        self.new_window2 = None
        self.new_window3 = None
        self.new_window4 = None
        self.new_window5 = None
        self.new_window6 = None
        self.new_window7 = None
        style = QApplication.setStyle("Fusion")

        # Impostazione di una palette di colori personalizzata
        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, QColor(234, 242, 248))  # Colore di sfondo
        self.palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # Colore del testo
        QApplication.setPalette(self.palette)

        self.new_window = None
        self.w: Wrapper = Wrapper()
        self.w.creaDipendente()
        self.w.creaMansione()
        self.w.creaReparto()

        self.server_label = QLabel('Server')
        self.server_input = QLineEdit()

        self.username_label = QLabel('Username')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Password')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.database_label = QLabel('Nome Database')
        self.database_input = QLineEdit()

        self.connect_button = QPushButton('Connect')
        self.connect_button.clicked.connect(self.connect)

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
        self.new_window1 = QWidget()
        self.new_window1.setWindowTitle('Inserisci Mansione')

        id_label = QLabel('ID:')
        id_input = QLineEdit()

        nome_label = QLabel('Nome:')
        nome_input = QLineEdit()

        tariffa_label = QLabel('Tariffa:')
        tariffa_input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(id_label)
        layout.addWidget(id_input)
        layout.addWidget(nome_label)
        layout.addWidget(nome_input)
        layout.addWidget(tariffa_label)
        layout.addWidget(tariffa_input)

        insert_button = QPushButton('Inserisci')
        insert_button.clicked.connect(
            lambda: self.insertMansione(id_input.text(), nome_input.text(), int(tariffa_input.text())))

        layout.addWidget(insert_button)

        self.new_window1.setLayout(layout)
        self.new_window1.show()

    def b2f(self):
        self.new_window2 = QWidget()
        self.new_window2.setWindowTitle('Inserisci Reparto')

        id_label = QLabel('ID:')
        id_input = QLineEdit()

        nome_label = QLabel('Nome:')
        nome_input = QLineEdit()

        responsabile_label = QLabel('Responsabile:')
        responsabile_input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(id_label)
        layout.addWidget(id_input)
        layout.addWidget(nome_label)
        layout.addWidget(nome_input)
        layout.addWidget(responsabile_label)
        layout.addWidget(responsabile_input)

        insert_button = QPushButton('Inserisci')
        insert_button.clicked.connect(
            lambda: self.insertReparto(id_input.text(), nome_input.text(), responsabile_input.text()))

        layout.addWidget(insert_button)

        self.new_window2.setLayout(layout)
        self.new_window2.show()

    def b3f(self):
        self.new_window3 = QWidget()
        self.new_window3.setWindowTitle('Inserisci Dipendente')

        id_matricola_label = QLabel('ID Matricola:')
        id_matricola_input = QLineEdit()

        cognome_label = QLabel('Cognome:')
        cognome_input = QLineEdit()

        nome_label = QLabel('Nome:')
        nome_input = QLineEdit()

        indirizzo_label = QLabel('Indirizzo:')
        indirizzo_input = QLineEdit()

        citta_label = QLabel('Città:')
        citta_input = QLineEdit()

        data_label = QLabel('Data:')
        data_input = QLineEdit()

        stipendio_label = QLabel('Stipendio:')
        stipendio_input = QLineEdit()

        anzianita_label = QLabel('Anzianità:')
        anzianita_input = QLineEdit()

        id_reparto_label = QLabel('ID Reparto:')
        id_reparto_input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(id_matricola_label)
        layout.addWidget(id_matricola_input)
        layout.addWidget(cognome_label)
        layout.addWidget(cognome_input)
        layout.addWidget(nome_label)
        layout.addWidget(nome_input)
        layout.addWidget(indirizzo_label)
        layout.addWidget(indirizzo_input)
        layout.addWidget(citta_label)
        layout.addWidget(citta_input)
        layout.addWidget(data_label)
        layout.addWidget(data_input)
        layout.addWidget(stipendio_label)
        layout.addWidget(stipendio_input)
        layout.addWidget(anzianita_label)
        layout.addWidget(anzianita_input)
        layout.addWidget(id_reparto_label)
        layout.addWidget(id_reparto_input)

        insert_button = QPushButton('Inserisci')
        insert_button.clicked.connect(lambda: self.insertDipendente(
            id_matricola_input.text(), cognome_input.text(), nome_input.text(), indirizzo_input.text(),
            citta_input.text(), data_input.text(), float(stipendio_input.text()), int(anzianita_input.text()),
            id_reparto_input.text()))

        layout.addWidget(insert_button)

        self.new_window3.setLayout(layout)
        self.new_window3.show()

    def b4f(self):
        self.new_window4 = QWidget()
        self.new_window4.setWindowTitle('Visualizza')

        table_label = QLabel('Nome della Tabella:')
        table_input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(table_label)
        layout.addWidget(table_input)

        insert_button = QPushButton('Visualizza')
        insert_button.clicked.connect(lambda: self.visualizzaTabella(table_input.text()))

        layout.addWidget(insert_button)

        self.new_window4.setLayout(layout)
        self.new_window4.show()

    def b5f(self):

        self.window5 = QWidget()
        layout = QVBoxLayout()

        for el in self.w.q1():
            label = QLabel(str(el))
            layout.addWidget(label)

        self.window5.setLayout(layout)
        self.window5.show()

    def b6f(self):
        result = self.w.q2()

        self.window6 = QWidget()
        layout = QVBoxLayout()

        for el in result:
            label = QLabel(f"Nome: {el[0]}, Cognome: {el[1]}")
            layout.addWidget(label)

        self.window6.setLayout(layout)
        self.window6.show()

    def b7f(self):
        result = self.w.q3()

        self.window7 = QWidget()
        self.window7.setWindowTitle("asd")
        layout = QVBoxLayout()

        for el in result:
            label = QLabel(f"Stipendio minimo: {el[0]}, Stipendio massimo: {el[1]}")
            layout.addWidget(label)

        self.window7.setLayout(layout)
        self.window7.show()

    def connect(self):

        self.new_windowa = QWidget()
        self.new_windowa.setWindowTitle('Connected')

        self.b1 = QPushButton('Inserisci Mansione')
        self.b2 = QPushButton('Inserisci Reparto')
        self.b3 = QPushButton('Inserisci Dipendenti')
        self.b4 = QPushButton('Visualizza')
        self.b5 = QPushButton('Calcolo dello stipendio medio')
        self.b6 = QPushButton('Elenco dei dipendenti')
        self.b7 = QPushButton('Calcolo dello stipendio minimo')

        layout = QVBoxLayout()
        for i, j in zip([self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7],
                        [self.b1f, self.b2f, self.b3f, self.b4f, self.b5f, self.b6f, self.b7f]):
            i.clicked.connect(j)
            layout.addWidget(i)

        self.new_windowa.setLayout(layout)

        self.new_windowa.show()


if __name__ == '__main__':
    # Cose di pyqt5
    app = QApplication(sys.argv)
    login = Application()
    login.show()
    sys.exit(app.exec_())
