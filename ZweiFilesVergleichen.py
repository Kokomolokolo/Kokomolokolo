"""#!/usr/bin/env python3
### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen

def drucke_liste(liste):
    print()
    # print(liste)
    # print()
    for element in liste:
        print(element)

def lies_file_ein_gib_liste_zurueck(file_name):
    liste_speicher_file = []
    with open(file_name, "r", encoding="utf8" ) as eingelesenes_file:
        liste_speicher_file.append(eingelesenes_file.read())
    string_in_liste = liste_speicher_file[0]
    rueckgabe_liste = string_in_liste.split("\n")
    return rueckgabe_liste
        
def loesche_doppelte_zeilen_einer_liste(liste):
    liste_ohne_doppelten = []
    for zeile in liste:
        if zeile not in liste_ohne_doppelten:
            liste_ohne_doppelten.append(zeile)
    return liste_ohne_doppelten

def loesche_schwellwert_9999999(liste):
    rueckgabe_liste = []
    for zeile in liste:
        if "Schwellwert 9999999" not in zeile:
            rueckgabe_liste.append(zeile)
    return rueckgabe_liste
    

def durchsuche_liste_ob_zeile_vorkommt(liste2, zeile):
    zaehler = 0
    for line in liste2:
        if zeile == line:
            zaehler += 1
    return zaehler

def durchlaufe_liste_1(liste1, liste2):
    for zeile in liste1:
        anzahl = durchsuche_liste_ob_zeile_vorkommt(liste2, zeile)
        if anzahl > 1:
            print(zeile)
        
    
###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    
    file_name = "Q_log.txt"
    log_file_liste = lies_file_ein_gib_liste_zurueck(file_name)
    log_file_liste_keine_doppelten = loesche_doppelte_zeilen_einer_liste(log_file_liste)
    
    liste_ohne_schwellwert = loesche_schwellwert_9999999(log_file_liste)
    drucke_liste(liste_ohne_schwellwert)
    # durchlaufe_liste_1(liste_ohne_schwellwert, log_file_liste)"""
