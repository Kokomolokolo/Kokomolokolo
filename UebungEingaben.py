### schebang line -  welcher Interpreter


### Hier stehen Importe

### Hier stehen Funktionen und Klassen

def ipn_eingabe_und_pruefen():
    while True:
        eingabe_ipn = input("Deine IPN :").strip()
        if len(eingabe_ipn) == 6:
            if eingabe_ipn[0] == "I":
                if eingabe_ipn[1:6].isnumeric():
                    print("Richtig")
                    return eingabe_ipn
        print()
        print("Keine gueltige IPN")
        print()

def vsnr_eingabe_und_pruefen():
    while True:
        eingabe_vsnr =input("Deine VSNR : ").strip()
        if len(eingabe_vsnr) == 12 and eingabe_vsnr[:8].isnumeric() and eingabe_vsnr[8].isalpha() and eingabe_vsnr[9:].isnumeric():
            print("Richtig")
            return eingabe_vsnr
        print()
        print("Keine gueltige")
        print()

###Hier steht das Hauptprogramm
if __name__ == '__main__':
    #Hier steht der Programmcode
    ipn = ipn_eingabe_und_pruefen()
    print(ipn)
    vsnr = vsnr_eingabe_und_pruefen()
    print(vsnr)
