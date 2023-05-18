from Wrapper import Wrapper

w = Wrapper()


def insertMansione(idM, nome, tariffa):
    l = [(idM, nome, tariffa)]
    w.insertMansione(l)


def insertReparto(idR, nome, responsabile):
    l = [(idR, nome, responsabile)]
    w.insertReparto(l)


def insertDipendente(idMa, cognome, nome, indirizzo, citta, data, stipendio, anzianità, idM, idR):
    l = [(idMa, cognome, nome, indirizzo, citta, data, stipendio, anzianità, idM, idR)]
    w.insertDipendente(l)


w.creaDipendente()
w.creaMansione()
w.creaReparto()
stop = False

while stop == False:
    c = int(input("1) Inserisci Mansione\n\
                  2) Inserisci Reparto\n\
                  3) Inserisci Dipendenti\n\
                  4) Visualizza \n \
                  5) Calcolo dello stipendio medio dei dipendenti raggruppati per città\n\
                  6) Elenco dei dipendenti che sono nati nel mese di aprile, maggio e giugno\n\
                  7) Calcolo dello stipendio minimo e massimo per ciascun reparto\n\
                  8) Esci\n\
                "))
    if c == 1:
        idM = input('Inserisci id\n')
        nome = input('Inserisci nome\n')
        tariffa = int(input('Inserisci Tariffa\n'))
        insertMansione(idM, nome, tariffa)

    elif c == 2:
        idR = input('insrisci id\n')
        nome = input('Inserisci nome\n')
        responsabile = input('Inserisci responsabile\n')
        insertReparto(idR, nome, responsabile)

    elif c == 3:
        idMa = input('Inserisci id matricola\n')
        cognome = input('inserisci cognome\n')
        nome = input('Insrisci nome')
        indirizzo = input('Inserisci indirizzo\n')
        citta = input('insrisci città')
        data = input('inserisci data\n')
        stipendio = input('Inserisci stipendio\n')
        anzianità = input('Inserisci anzianità')
        idM = input('Inserisci id matricola\n')
        idR = input('Inserisci id reparto\n')
        insertDipendente(idMa, cognome, nome, indirizzo, citta, data, stipendio, anzianità, idM, idR)

    elif c == 4:
        nometabella = input("Inserisci il nome della tabella che vuoi visualizzare")
        tabella = w.visualizza_tabella(nometabella)
        print(tabella)

    elif c == 5:
        try:
            w.q1()
            print("Quary eseguita con successo!")
        except:
            print("ERRORE")
    elif c == 6:
        try:
            w.q2()
            print("Quary eseguita con successo!")
        except:
            print("ERRORE")
    elif c == 7:
        try:
            w.q3()
            print("Quary eseguita con successo!")
        except:
            print("ERRORE")

    elif c == 8:
        stop = True

