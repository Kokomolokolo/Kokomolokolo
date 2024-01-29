### Hier stehen Importe

### Hier stehen Funktionen und Klassen
def drucke_liste(liste):
    print()
    for element in liste:
        print(element)
        
def zwei_matrizen_ausdrucken(matrix1, matrix2):
    dim = len(matrix1)
    for zeile in range(dim):
        eine_zeile = ""
        andrer_zeile = ""
        eine_ganze_zeile = ""
        for spalte in range(dim):
            eine_zeile += str(matrix1[zeile][spalte]) + "  "
            andrer_zeile += str(matrix2[zeile][spalte]) + "  "
            eine_ganze_zeile = eine_zeile + "  " +  andrer_zeile 
        print(eine_ganze_zeile)
             
def eine_matrix_ausdrucken(matrix):
    dim = len(matrix)
    for zeile in range(dim):
        eine_zeile = ""
        andrer_zeile = ""
        eine_ganze_zeile = ""
        for spalte in range(dim):
            eine_zeile += str(matrix[zeile][spalte]) + "  "            
        print(eine_zeile)
        
def spalte_aus_matrix_auslesen(matrix, index):
    rueckgabe_liste = []
    for zeile in matrix:
        rueckgabe_liste.append(zeile[index])
    return rueckgabe_liste
    
def zeile_aus_matrix_auslesen(matrix, index):
    return matrix[index]
    
def matrizen_zeile_mal_spalte_multiplizieren(zeile_liste, spalte_liste):
    summe = 0
    for i in range(len(zeile_liste)):
        summe += zeile_liste[i] * spalte_liste[i]
    return summe

def erstelle_null_matrix(laenge):
    zeile = []
    for i in range(laenge):
        zeile.append(0)
    matrix = []
    for i in range(laenge):
        matrix.append(zeile.copy())
    return matrix

def matrix_multiplikation(matrix1, matrix2):
    am = []
    ausgabe_matrix = erstelle_null_matrix(len(matrix2))
    for index_spalte in range(len(matrix1)):
        for index_zeile in range(len(matrix1)):
            z = zeile_aus_matrix_auslesen(matrix1, index_zeile)
            s = spalte_aus_matrix_auslesen(matrix2, index_spalte)
            ausgabe_matrix[index_zeile][index_spalte] = matrizen_zeile_mal_spalte_multiplizieren(z, s)
            e = matrizen_zeile_mal_spalte_multiplizieren(z, s)
    return ausgabe_matrix


###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    m1 = [[1, 8],[5, 7]]
    m2 = [[5, 4],[3, 1]]
    
    """m1 = [[1, 2, 0], [3, 4, 7], [2, 1, 3]]
    m2 = [[8, 4, 1], [1, 0, 3], [2, 2, 0]]"""
    #m1 = [[1,2,0,3], [3, 4, 7, 9], [2, 1, 3, 4], [1, 2, 3, 6]]
    #m2 = [[1, 0, 0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
    
    print("Die Matrixen")
    zwei_matrizen_ausdrucken(m1, m2)
    print("===================")
    m_ausgabe = matrix_multiplikation(m1, m2)
    eine_matrix_ausdrucken(m_ausgabe)
    
    
