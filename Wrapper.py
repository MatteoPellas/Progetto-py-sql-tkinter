import pymssql

class Wrapper:

    conn = 0
    #192.168.40.16\sqlexpress
    #5.172.64.20\sqlexpress

    def __init__(self, server = "5.172.64.20\sqlexpress",user = "4FI_Pellas", password = "xxx123##", database = "4FI_Pellas"):
        self._server = server
        self._user = user
        self._password = password
        self._database = database

    def connessione(self):
        try:
            Wrapper.conn = pymssql.connect(server = self._server, user = self._user, password = self._password, database = self._database)
            print("\nConnessione effettuata DB DB4FI!\n")
            return Wrapper.conn
        
        except:
            print("connessione non riuscita")
            return 0
        
    def disconnessione(self, co):
	
        try:
            co.close()
            print("\nCHIUSURA Connessione effettuata DB DB4FI!\n")
            
        except:
            print("\nCHIUSURA Connessione NON riuscita DB DB4FI!\n")
            return 0
        

    def creaMansione(self):
        c = self.connessione()
        try:
            ope = """
                IF NOT EXISTS ( 
                    Select * 
                     from sysobjects 
                     where xtype = 'U' and name = 'Persona' 
                    )
                CREATE TABLE Persona (
                    Id_Mansione varchar(20) primary key,
                    Nome varchar(20),
                    Taiffa_oraria decimal
                    )
                    """
            cursore= c.cursor()
            cursore.execute(ope)
            c.commit()
            print("\nCREATE effettuata (o la tabella esiste) su DB DB4FI!\n")
        except:
            print("errore")
        self.disconnessione(c)

    def creaReparto(self):
        ok = 1
        c = self.connessione()
        try:
            ope = """
                IF NOT EXISTS ( 
                    Select * 
                     from sysobjects 
                     where xtype = 'U' and name = 'Conferenza' 
                    )
                CREATE TABLE Conferenza (
                    Id_Reparto varchar(20) primary key,
                    Nome varchar(20),
                    Responsabile varchar(20)
                    )
                    """
            cursore= c.cursor()
            cursore.execute(ope)
            c.commit()
            print("\nCREATE effettuata (o la tabella esiste) su DB DB4FI!\n")
        except:
            print("errore")
        self.disconnessione(c)

    def creaDipendente(self):
        
        c = self.connessione()
        try:
            ope = """
                IF NOT EXISTS ( 
                    Select * 
                     from sysobjects 
                     where xtype = 'U' and name = 'Iscrizione' 
                    )
                Iscrizione(
                    Id_marticola varchar(20) primary key,
                    Cognome varchar(20),
                    Nome varchar(20),
                    Indirizzo varchar(20),
                    Città varchar(20),
                    Data_Nascita date,
                    Stipendio decimal,
                    Anzianità decimal,
                    Id_mansione varchar(20),
                    Id_Reparto varchar(20),
                    FOREIGN KEY (Id_mansione) references Mansione (Id_Mansione),
                    FOREIGN KEY (Id_Reparto) references Reparto (Id_Reparto)
                    )
                    """
            cursore= c.cursor()
            cursore.execute(ope)
            c.commit()
            print("\nCREATE effettuata (o la tabella esiste) su DB DB4FI!\n")
        except:
            print("errore")
        self.disconnessione(c)

    def insertMansione(self, parametro):
        try:
            # Connessione
            #WrapperDB4D.conn = self.connetti() 
            c = self.connessione() 
            cursore = c.cursor()
            # NB %d anche per i DECIMAL!!!!!!!
            
            insertParametrica = " INSERT INTO Persona VALUES (%s , %s , %d  ) "
            print(parametro)
            if  isinstance(parametro, tuple)  : # UNA sola riga
                print("E' UNA TUPLA")
                
                cursore.execute(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGA AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            elif  isinstance(parametro, list)    : # pi˘ righe
                print("E' UNA LISTA")
                cursore.executemany(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGHE AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            else:
                # Disconnessione
                self.disconnessione(c)
                return "KO parametro"
        except:
            print("\nPROC Inserimento/i: PROBLEMA !")
            self.disconnessione(c)
            return "KO"
        
        
    def insertReparto(self, parametro):
        try:
            # Connessione
            #WrapperDB4D.conn = self.connetti() 
            c = self.connessione() 
            cursore = c.cursor()
            # NB %d anche per i DECIMAL!!!!!!!
            
            insertParametrica = " INSERT INTO Conferenza VALUES (%s , %s , %s  ) "
            print(parametro)
            if  isinstance(parametro, tuple)  : # UNA sola riga
                print("E' UNA TUPLA")
                
                cursore.execute(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGA AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            elif  isinstance(parametro, list)    : # pi˘ righe
                print("E' UNA LISTA")
                cursore.executemany(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGHE AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            else:
                # Disconnessione
                self.disconnessione(c)
                return "KO parametro"
        except:
            print("\nPROC Inserimento/i: PROBLEMA !")
            self.disconnessione(c)
            return "KO"
       
        
    def insertDipendente(self, parametro):
        try:
            # Connessione
            #WrapperDB4D.conn = self.connetti() 
            c = self.connessione() 
            cursore = c.cursor()
            # NB %d anche per i DECIMAL!!!!!!!
            
            insertParametrica = " INSERT INTO Iscrizione VALUES (%s , %s , %s , %s, %s , %s  , %d , %d ; %s , %s ) "
            print(parametro)
            if  isinstance(parametro, tuple)  : # UNA sola riga
                print("E' UNA TUPLA")
                
                cursore.execute(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGA AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            elif  isinstance(parametro, list)    : # pi˘ righe
                print("E' UNA LISTA")
                cursore.executemany(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGHE AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            else:
                # Disconnessione
                self.disconnessione(c)
                return "KO parametro"
        except:
            print("\nPROC Inserimento/i: PROBLEMA !")
            self.disconnessione(c)
            return "KO"
        
    def visualizza_tabella(self,nome_tabella):
        c = self.connessione()
        cursore = c.cursor()
        try:
            cursore.execute(f"SELECT * FROM {nome_tabella}")
            result = cursore.fetchall()
            return result
        except:
            print("Errore durante l'interrogazione del database")
            return 0
        finally:
            self.disconnessione(c)
        

    def q1(self):
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            istru = """ 
                select AVG(Stipendio)
                from Dipendente
                group by citta
               
                """
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    
    def q2(self):
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            istru = """ 
                select Nome, Cognome
                from Dipendente
                where Data_nascita between motd(04)
               
                """
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    
    def q3(self):
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            istru = """ 
                select min(d.stipendio), max(d.stipendio)
                from Dipendente as d
                join Reparto as r
                on d.Id_Reparto = r.Id_Reparto
                group by r.Nome
               
                """
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
"""
a. Calcolo dello stipendio medio dei dipendenti raggruppati per città
b. Elenco dei dipendenti che sono nati nel mese di aprile, maggio e giugno(valori
inseriti anche da input)
c. Calcolo dello stipendio minimo e massimo per ciascun reparto
"""
        
        
    