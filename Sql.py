### schebang line -  welcher Interpreter


### Hier stehen Importe
#import sqlite3


### Hier stehen Funktionen und Klassen

def erstelle_eine_datenbank(namen):
    ## Verbindung zu Datenbank herrstellen (öffnen)
    ## ist diese noch nicht angelegt
    ## wird sie automatisch erstellt
    connection = sqlite3.connect(namen)
    ## Cursor (Objekt/Klasse) wird erstellt
    cursor = connection.cursor()
    ## Cursor (Objekt/Klasse) wird erstellt
    
    ## Erstelle eine Tabelle in der Datenbank
    # sql_befehl = "CREATE TABLE physiker(Name TEXT, Fachgebiet TEXT, IQ INTAGER);"
    sql_befehl = "CREATE TABLE IF NOT EXISTS physiker(Name TEXT, Fachgebiet TEXT, IQ INTAGER);"
    ## SQL Befehl ausführen
    cursor.execute(sql_befehl)
  
    ## Bestätigung eines Änderungsbefehls in einer Tabelle
    cursor
    
    ## Cursor wird beendet
    cursor.close()
    ## Verbindung zur DB wird geschlossen
    connection.close()

def schreibe_in_eine_tabelle(namen_db, name_tabelle, daten1, daten2, daten3):
    connection = sqlite3.connect(namen_db)
    cursor = connection.cursor()
    
    # sql_befehl = "INSERT INTO physiker(name, fachgebiet, iq) VALUES('Neawton', 'Kräfte', '143');
    sql_befehl = "INSERT INTO " + name_tabelle + "(name, fachgebiet, iq) VALUES('" + daten1 + "', '" +  daten2 + "', '" + str(daten3) + "')"+ ";"
    print(sql_befehl)
    cursor.execute(sql_befehl)
    ## Bestätigung eines Änderungsbefehls in einer Tabelle
    connection.commit()
    
    cursor.close()
    connection.close()

def veraendere_daten_in_einer_tabelle(namen_db, name_tabelle):
    connection = sqlite3.connect(namen_db)
    cursor = connection.cursor()
    
    sql_befehl = "UPDATE physiker SET fachgebiet = 'Atomphysiker' WHERE iq > 140;"
    cursor.execute(sql_befehl)
    
    connection.commit()
    
    cursor.close()
    connection.close()

def losche_zeilen_in_tabelle(name_db, namen_tabelle):
    connection = sqlite3.connect(namen_db)
    cursor = connection.cursor()
    
    ## Loeschen von Datensätzen
    sql_befehl = "DELETE from physiker WHERE name = 'Joule';"
    sql_befehl = "DELETE from physiker;"
    cursor.execute(sql_befehl)
    
    connection.commit()
    
    cursor.close()
    connection.close()

def lies_aus_einer_tabelle(name_db, namen_tabelle, suchbegriff):
    rueckgabe_liste = []
    
    connection = sqlite3.connect(namen_db)
    cursor = connection.cursor()
    
    # sql_befehl = "SELECT * from physiker; "
    sql_befehl = "SELECT * from " + name_tabelle + ";"
    # sql_befehl = "SELECT name from physiker WHERE fachgebiet = 'Kräfte';"
    print(sql_befehl)
    cursor.execute(sql_befehl)
    
    for zeile in cursor:
        rueckgabe_liste.append(zeile)
    
    
    cursor.close()
    connection.close()
    return rueckgabe_liste

def druck_sql_ergebis_aus(ergebnis_liste):
    for tupel in ergebnis_liste:
        print(tupel)
    
###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    print("Hallo Welt")
    namen_db = "test1.db"
    name_tabelle = "physiker"
    erstelle_eine_datenbank(namen_db)
    
    schreibe_in_eine_tabelle(namen_db, name_tabelle, "Neawton","Kräfte",143)
    schreibe_in_eine_tabelle(namen_db, name_tabelle, "Einstein", "Relativitätstheorie", 141)
    schreibe_in_eine_tabelle(namen_db, name_tabelle, "Ampere", "Elektrizität", 136)
    schreibe_in_eine_tabelle(namen_db, name_tabelle, "Joule", "Kräfte", 139)
    
    veraendere_daten_in_einer_tabelle(namen_db, name_tabelle)
    
    
    
    ergebnis = lies_aus_einer_tabelle(namen_db, name_tabelle, "")
    druck_sql_ergebis_aus(ergebnis)
    print(len(ergebnis))
    
    losche_zeilen_in_tabelle(namen_db, name_tabelle)
    
    ergebnis = lies_aus_einer_tabelle(namen_db, name_tabelle, "")
    druck_sql_ergebis_aus(ergebnis)
