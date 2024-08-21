# Variabel definieren
umrechnungsfaktor1 = 1
umrechnungsfaktor1000 = 1000

neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ")
if neueEingabe == "Ja":
    
# Umrechnung von Liter in Kubikdezimeter und Kubikmeter
    wahl = input("gib eine Auswahl zwischen Liter, Kubikdezimeter oder Kubikmeter an: ")
    if wahl == "Liter":
        inputLiter = float(input("Gib den Wert in Liter an: "))
        outputKubikdezi = inputLiter * umrechnungsfaktor1
        print(inputLiter,"Liter sind",outputKubikdezi,"dm³")
        outputKubikmeter = inputLiter / umrechnungsfaktor1000
        print(inputLiter,"Liter sind",outputKubikmeter,"m³")

# Umrechnung von Kubikdezimeter in Liter und Kubikmeter
    elif wahl == "Kubikdezimeter":
        inputKubikdezi = float(input("Gib den Wert in Kubikdezimeter an: "))
        outputLiter = inputKubikdezi * umrechnungsfaktor1
        print(inputKubikdezi,"dm³ sind",outputLiter,"Liter")
        outputKubikmeter = inputKubikdezi / umrechnungsfaktor1000
        print(inputKubikdezi,"dm³ sind",outputKubikmeter,"m³")
    
# Umrechnung von Kubikmeter in Liter und Kubikdezimeter
    elif wahl == "Kubikmeter":
        inputKubikmeter = float(input("Gib den Wert in Kubikmeter an: "))
        outputLiter = inputKubikmeter * umrechnungsfaktor1000
        print(inputKubikmeter,"m³ sind",outputLiter,"Liter")
        outputKubikdezimeter = inputKubikmeter * umrechnungsfaktor1000
        print(inputKubikmeter,"m³ sind",outputKubikdezimeter,"dm³")

neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ")
        #if neueEingabe == "Ja":
            #return  
        
#neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ")
    #if neueEingabe == "Ja":