"""#!/usr/bin/env python3
### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen

def drucke_liste(liste):
    print()
    print(liste)
    print()
    for element in liste:
        print(element)

def lies_file_ein_gib_liste_zurueck(file_name):
    liste_speicher_file = []
    with open(file_name, "r", encoding="utf8" ) as eingelesenes_file:
        liste_speicher_file.append(eingelesenes_file.read())
    string_in_liste = liste_speicher_file[0]
    rueckgabe_liste = string_in_liste.split("\n")
    return rueckgabe_liste

def drucke_alle_importe(log_file):
    rueckgabe_liste = []
    for log in log_file:
        if "IMPORT" in log:
            rueckgabe_liste.append(log)
            print(log)
    return rueckgabe_liste
    
def drucke_alle_exporte(log_file):
    rueckgabe_liste = []
    for log in log_file:
        if "EXPORT" in log:
            rueckgabe_liste.append(log)
            print(log)
    return rueckgabe_liste

def erstelle_liste_ohne_Schwellwert_9999999(log_file):
    rueckgabe_liste = []
    for log in log_file:
        if "wird entsprechend Schwellwert 9999999 gesetzt" not in log:
            # print(log)
            rueckgabe_liste.append(log)
    return rueckgabe_liste

def erstelle_liste_ERROR(log_file):
    rueckgabe_liste = []
    for log in log_file:
        if "ERROR" in log:
            rueckgabe_liste.append(log)
    return rueckgabe_liste

def finde_gleiche_zeilen(log_file):
    rueckgabe_liste = [] 
    liste_doppelte = []
    for zeile in log_file:
        if zeile in rueckgabe_liste:
            liste_doppelte.append(zeile)
        else:
            rueckgabe_liste.append(zeile)
    return liste_doppelte
""""""
def loesche_doppelten(log_file):
    liste_ohne_doppelten = list(set(liste_mit_zeilen_des_files))
    liste_der_doppelten = []
    print(liste_ohne_doppelten)
    for zeile in log_file:
        if zeile not in liste_ohne_doppelten:
            liste_der_doppelten.append(zeile)
    return liste_der_doppelten
    """
"""
def element_aus_kd():
    liste_ohne_doppelten = list(set(liste_mit_zeilen_des_files))
    for element in liste_ohne_doppelten:   
    return liste_ohne_doppelten
"""
"""
def anzahl_vorkommen_einer_zeile(log_file, liste_ohne_doppelten):
    index = 0
    rueckgabe_liste = []
    for zeile in log_file:
        if zeile in liste_ohne_doppelten[index]:
            rueckgabe_liste.append(zeile)
        index += 1
    return rueckgabe_liste

def anzahl_zeile(log_file):
    for zeile in log_file:
        if 
        
""""""
def anzahl_einer_zeile(log_file, liste_ohne_doppelten):
    index = 0
    liste_der_doppelten = []
    for zeile in liste_ohne_doppelten:
        if zeile not in liste_ohne_doppelten[index]:
            liste_der_doppelten.append(zeile)
        index += 1
    return liste_der_doppelten

###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    
    file_name = "log_file.txt"
    liste_mit_zeilen_des_files = lies_file_ein_gib_liste_zurueck(file_name)
    #liste_mit_importen = drucke_alle_importe(liste_mit_zeilen_des_files)
    #liste_mit_exporten = drucke_alle_exporte(liste_mit_zeilen_des_files)
    #liste_ohne_unnuetz = erstelle_liste_ohne_Schwellwert_9999999(liste_mit_zeilen_des_files)
    #liste_fehler_ohne_unnuetz = erstelle_liste_ERROR(liste_ohne_unnuetz)
    #liste_doppelte_zeile = finde_gleiche_zeilen(liste_ohne_unnuetz)
    #liste_der_doppelten = loesche_doppelten(liste_mit_zeilen_des_files)
    
    liste_ohne_doppelten = list(set(liste_mit_zeilen_des_files))
    liste_der_doppelten = anzahl_einer_zeile(liste_mit_zeilen_des_files, liste_ohne_doppelten)
    drucke_liste(liste_der_doppelten)
    #liste_der_doppelten = anzahl_vorkommen_einer_zeile(liste_mit_zeilen_des_files, liste_ohne_doppelten)
    

    
    drucke_liste(liste_der_doppelten)"""
    
