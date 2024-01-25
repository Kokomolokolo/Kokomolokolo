"""#!/usr/bin/env python3
### das ist die shebang line, sie sagt an, welcher Interpreter benutzt wird und wo er steht


### Hier stehen Importe


### Hier stehen Funktionen und Klassen

def druck_eine_liste_aus(liste):
    print(liste)
    print()
    for zahl in liste:
        print(zahl)
    print()

def erstelle_die_zahlen_liste(laenge):
    liste = list(range(laenge))
    return liste

def druck_die_geraden_zahlen_einer_liste_aus(liste):
    print()
    for zahl in liste:
        if zahl % 2 == 0:
            print(zahl)
    print() 
 

def erstelle_liste_mal_3(liste):
    rueckgabe_liste = []
    for zahl in liste:
        rueckgabe_liste.append(zahl * 3)
    return rueckgabe_liste

def erstelle_liste_ungerade_zahlen(liste):
    rueckgabe_liste = []
    for zahl in liste:
        if zahl % 2 == 1:
            rueckgabe_liste.append(zahl)
    return rueckgabe_liste
 
 
### Hier steht das Hauptprogramm
if __name__ == "__main__":
    ### Hier steht der Code vom Hauptprogramm

    ### Grundwerte und Variablen
    anzahl_elemente = 30
    zahlen_liste = erstelle_die_zahlen_liste(anzahl_elemente)
    ausgabe_liste = []


    ### Programmablauf

    # lies zahlen_liste und schreibe Werte * 3 in ausgabe_liste
    ausgabe_liste = erstelle_liste_mal_3(zahlen_liste)


    # druck die gesamte ausgabe_liste aus und auch einzeln nacheinander
    druck_eine_liste_aus(zahlen_liste)
    druck_eine_liste_aus(ausgabe_liste)

    # druck alle gerade zahlen aus ausgabe_liste aus
    druck_die_geraden_zahlen_einer_liste_aus(ausgabe_liste)

    # druck alle ungerade Zahlen aus
    print("Ungerade Zahlen")
    liste_ungerade_zahlen = erstelle_liste_ungerade_zahlen(ausgabe_liste)
    druck_eine_liste_aus(liste_ungerade_zahlen)
    print("ENDE")"""
 
