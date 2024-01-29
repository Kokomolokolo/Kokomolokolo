### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen

### Aufgabe
# benutze nur das for x in liste Konstrukt
# Erstelle eine Liste mit Fotonamen, 100 Stück
# Format erstes Bild: 001_Image.jpg
# achte auf die führenden Nullen
# nutze Befehl string.zfill(3)

def erstelle_liste_image_name(laenge):
    liste_zahlen = list(range(1,laenge + 1))
    rueckgabe_liste = []
    for zahl in liste_zahlen:
        bild_name = (str(zahl).zfill(3) + "image.jpg")
        rueckgabe_liste.append(bild_name)  
    return rueckgabe_liste

def drucke_liste(liste):
    print()
    print(liste)
    print()
    for element in liste:
        print(element)

def erstlle_datum_an_bildname_anhaengen(liste_bildernamen):
    rueckgabe_liste = []
    for bild in liste_bildernamen:
        bild_name_mit_datum = bild[:3] + "_" + "2024-01-19_" + bild[3:]
        rueckgabe_liste.append(bild_name_mit_datum)
    return rueckgabe_liste

def erstellen_uhrzeit_an_bildname_anhaengen(liste_bildernamen_datum):
    rueckgabe_liste = []
    for bildname in liste_bildernamen_datum:
        bild_name_mit_uhrzeit = (bildname[:15] + "00:00:00" + bildname[15:])
        rueckgabe_liste.append(bild_name_mit_uhrzeit)
    return rueckgabe_liste #100_2024-01-19_08:17:02_image.jpg


def umstellen_datum_uhrzeit_zahl_jpg(liste_bildernamen_datum_uhrzeit):
    rueckgabe_liste = []
    for bildname in liste_bildernamen_datum_uhrzeit:
        bild_name_neu = bildname[4:10] + bildname[10:23] + "_" + bildname[:3] + "_" + bildname[23:]
        rueckgabe_liste.append(bild_name_neu)
    return rueckgabe_liste # 2024-01-19_00:00:00_100_image.jpg

def erstelle_liste_uhrzeiten(laengen):
    sekunde = 0
    minute = 0
    stunde = 0
    liste_uhrzeiten = list(range(1,laengen + 1))
    rueckgabe_liste = []
    for zahl in liste_uhrzeiten:
        str_uhrzeit_neu = str(stunde).zfill(2) + ":" +  str(minute).zfill(2) + ":" + str(sekunde).zfill(2)
        sekunde = sekunde + 1
        if sekunde == 60:
            sekunde = 0
            minute = minute + 1
        if minute == 60:
            minute = 0
            stunde = stunde + 1
        rueckgabe_liste.append(str_uhrzeit_neu)
    return rueckgabe_liste

def mache_neu_uhrzeit(liste_uhrzeiten, liste_reihenfolge_datum_uhrzeit_nummer_jpg):
    index = 0
    rueckgabe_liste = []
    for bild in liste_reihenfolge_datum_uhrzeit_nummer_jpg:
        bild_name_neu = bild[:11] + str(liste_uhrzeiten[index]) + "_" + bild[20:]
        rueckgabe_liste.append(bild_name_neu)
        index += 1
    return rueckgabe_liste

def erstelle_liste_ohne_zahl(liste_datum_uhrzeitneu_nummer_jpg):
    rueckgabe_liste = []
    for bild in liste_datum_uhrzeitneu_nummer_jpg:
        bild_name_neu = bild[:20] + bild[24:]
        rueckgabe_liste.append(bild_name_neu)
    return rueckgabe_liste
    
    
###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    anzahl_der_bilder = 100 
    liste_bildernamen = erstelle_liste_image_name(anzahl_der_bilder)
    liste_bildernamen_datum = erstlle_datum_an_bildname_anhaengen(liste_bildernamen)
    liste_bildernamen_datum_uhrzeit = erstellen_uhrzeit_an_bildname_anhaengen(liste_bildernamen_datum)
    liste_reihenfolge_datum_uhrzeit_nummer_jpg = umstellen_datum_uhrzeit_zahl_jpg(liste_bildernamen_datum_uhrzeit)
    liste_uhrzeiten = erstelle_liste_uhrzeiten(laengen = 100)
    liste_datum_uhrzeitneu_nummer_jpg = mache_neu_uhrzeit(liste_uhrzeiten, liste_reihenfolge_datum_uhrzeit_nummer_jpg)
    liste_datum_uhrzeitneu_ohne_nummer_jpg = erstelle_liste_ohne_zahl(liste_datum_uhrzeitneu_nummer_jpg)
    
    drucke_liste(liste_datum_uhrzeitneu_ohne_nummer_jpg)
    
    
