"""#!/usr/bin/env python3
### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen und Klassen
class Quarkus_log_liste():
    def __init__(self):
        self.file_name =  "Q_log.txt"
        self.quarkus_log_liste = self.lies_file_ein_und_gib_quarkus_als_liste_zurueck(self.file_name)
        self.liste_quarkus_ohne_schwellwert_9 =self.bereinige_quarkus_log_um_schwellwert_9999999(self.quarkus_log_liste)
        self.liste_quarkus_exporte = self.finde_alle_exporte(self.liste_quarkus_ohne_schwellwert_9)
        self.liste_quarkus_importe = self.finde_alle_importe(self.liste_quarkus_ohne_schwellwert_9)
        self.liste_quarkus_sonstige = []
        
        
    def lies_file_ein_und_gib_quarkus_als_liste_zurueck(self, file_name):
        liste_speicher_file = []
        with open(file_name, "r", encoding="utf8") as eingelesenes_file:
            liste_speicher_file.append(eingelesenes_file.read())
        string_in_liste = liste_speicher_file[0]
        rueckgabe_liste = string_in_liste.split("\n")
        return rueckgabe_liste
    """"""
    def liefere_ERROR_export(self,liste):
        rueckgabe_liste = []
        for zeile in liste:
            if "ERROR" in zeile:
                rueckgabe_liste.append(zeile)
        return rueckgabe_liste
    """"""
    def finde_alle_importe(self, log_file):
        rueckgabe_liste = []
        for log in log_file:
            if "IMPORT" in log:
                rueckgabe_liste.append(log)
        return rueckgabe_liste
    
    def finde_alle_exporte(self, log_file):
        rueckgabe_liste = []
        for log in log_file:
            if "EXPORT" in log:
                rueckgabe_liste.append(log)
        return rueckgabe_liste  
    
    def bereinige_quarkus_log_um_schwellwert_9999999(self, liste):
        rueckgabe_liste = []
        for zeile in liste:
            if "Schwellwert 9999999" not in zeile:
                rueckgabe_liste.append(zeile)
        return rueckgabe_liste
        
    ### Getter und setter
    def get_quarkus_log_liste(self):
        return self.quarkus_log_liste
    
    def get_quarkus_exporte(self):
        return self.liste_quarkus_exporte
    
    def get_quarkus_importe(self):
        return self.liste_quarkus_importe
    
    
def drucke_liste(liste):
    for element in liste:
        print(element)   
  
###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    Qlog = Quarkus_log_liste().get_quarkus_log_liste()
    
    liste_exporte = Quarkus_log_liste().get_quarkus_exporte()
    liste_importe = Quarkus_log_liste().get_quarkus_importe()
    
    drucke_liste(liste_importe)
    drucke_liste(liste_exporte)
    
    
    
    
