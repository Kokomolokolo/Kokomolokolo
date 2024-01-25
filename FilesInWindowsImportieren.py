"""#!/usr/bin/env python3
### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen

def lies_file_ein_gib_liste_zurueck(file_name):
    liste_speicher_file = []
    with open(file_name, "r", encoding="utf8" ) as eingelesenes_file:
        liste_speicher_file.append(eingelesenes_file.read())
    string_in_liste = liste_speicher_file[0]
    rueckgabe_liste = string_in_liste.split("\n")
    return rueckgabe_liste


###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    
    file_name = "log_file.txt"
    liste_mit_zeilen_des_files = lies_file_ein_gib_liste_zurueck(file_name)
    for zeile in liste_mit_zeilen_des_files:
        print(zeile)"""
