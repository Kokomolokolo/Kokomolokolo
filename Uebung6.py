"""#!/usr/bin/env python3
### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen

def drucke_liste(liste):
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
    
def finde_alle_importe(log_file):
    rueckgabe_liste = []
    for zeile in log_file:
        if "IMPORT" in zeile:
            rueckgabe_liste.append(zeile)
    return rueckgabe_liste

def finde_alle_exporte(log_file):
    rueckgabe_liste = []
    for zeile in log_file:
        if "EXPORT" in zeile:
            rueckgabe_liste.append(zeile)
    return rueckgabe_liste

def finde_ohne_import_oder_export(log_file):
    rueckgabe_liste = []
    for zeile in log_file:
        if "EXPORT" not in zeile and "IMPORT" not in zeile:
            rueckgabe_liste.append(zeile)
    return rueckgabe_liste

def loesche_schwellwert_9999999(liste):
    rueckgabe_liste = []
    for zeile in liste:
        if "Schwellwert 9999999" not in zeile:
            rueckgabe_liste.append(zeile)
    return rueckgabe_liste

###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    
    file_name = "Q_log.txt"
    liste_mit_zeilen_des_files = lies_file_ein_gib_liste_zurueck(file_name)
    liste_zeilen_files_ohne_schwellwert = loesche_schwellwert_9999999(liste_mit_zeilen_des_files )
    liste_importe = finde_alle_importe(liste_mit_zeilen_des_files)
    liste_exporte = finde_alle_exporte(liste_zeilen_files_ohne_schwellwert)
    liste_ohne_export_import = finde_ohne_import_oder_export(liste_mit_zeilen_des_files)
    
    
    
    print("Exporte")
    drucke_liste(liste_exporte)
    print()
    print(len(liste_importe))
    drucke_liste(liste_importe)
    print()
    print("Anderes")
    drucke_liste(liste_ohne_export_import)
    print("Anzahl Importe", len(liste_importe))
    print("Anzahl Exporte", len(liste_exporte))
    print("Anzahl Andere", len(liste_ohne_export_import))"""



