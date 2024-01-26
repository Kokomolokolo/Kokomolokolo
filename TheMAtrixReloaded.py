" schebang line -  welcher Interpreter


" Hier stehen Importe

"Hier stehen Funktionen und Klassen

def matrixen1_ausdrucken(matrix1, matrix2):
    dim = len(matrix1)
    for zeile in range(dim):
        eine_zeile = ""
        andrer_zeile = ""
        eine_ganze_zeile = ""
        for spalte in range(dim):
            eine_zeile += str(matrix1[zeile][spalte]) + "  "
            andrer_zeile += str(matrix2[spalte][zeile]) + "  "
            eine_ganze_zeile = eine_zeile + "  " +  andrer_zeile
            
        print(eine_ganze_zeile)
        
            
    " print("(", element_aussen[0], element_aussen[1], element_aussen[2],")", "*", matrixen2_ausdrucken(m2))


def matrixen_miteinader_mutiplizieren(matrix1, matrix2):
    dim = 3
    for zeile in range(dim):
        eine_zeile_fertig = ""
        andrer_zeile = ""
        eine_ganze_zeile = ""
        for spalte in range(dim):
            
        print(eine_zeile_fertig)
            


"Hier steht das Hauptprogramm
if __name__ == '__main__':
    "Hier steht der Programmcode
    print("Hallo Welt")
    m1 = [[1, 2, 0], [3, 4, 7], [2, 1, 3]]
    m2 = [[8, 1, 2], [4, 0, 2], [1, 3, 0]]


    matrixen1_ausdrucken(m1, m2)
    matrixen_miteinader_mutiplizieren(m1, m2)
