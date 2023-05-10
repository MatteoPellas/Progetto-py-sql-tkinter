from Wrapper import Wrapper
w = Wrapper()

def insertMansione(idM, nome, tariffa ):
    l= [(idM,nome,tariffa)]
    w.insertMansione(l)
    
def insertReparto(idR, nome, responsabile):
    l = [(idR, nome, responsabile)]
    w.insertReparto(l)
    
def insertDipendente(idMa, cognome, nome, indirizzo, citta, data, stipendio, anzianità, idM, idR):
    l = [(idMa, cognome, nome, indirizzo, citta, data, stipendio, anzianità, idM, idR)]
    w.insertDipendente(l)
    
def Main():
    w.creaDipendente()
    w.creaMansione()
    w.creaReparto()
    stop = False
    
    while stop == False:
        c = int(input("1) Inserisci Mansione\n\
                      2) Inserisci Reparto\n\
                      3) Inserisci Dipendenti\n\
                      4) Visualizza \
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
            idR= input('Inserisci id reparto\n')
            insertDipendente(idMa, cognome, nome, indirizzo, citta, data, stipendio, anzianità, idM, idR)
            
        elif c == 4:
            nometabella=input("Inserisci il nome della tabella che vuoi visualizzare")
            tabella=w.visualizza_tabella(nometabella)
            print(tabella)
                                
Main()
        
# TEST
# TEST
