# Variabel definieren
umrechnungsfaktor1 = 1
umrechnungsfaktor1000 = 1000

# while-Schleife
eingabeJaNein = 1
while eingabeJaNein == 1:

# Umrechnung von Liter in Kubikdezimeter und Kubikmeter
    wahl = input("gib eine Auswahl zwischen Liter, Kubikdezimeter oder Kubikmeter an: ").lower()
    if wahl == "liter":
        inputLiter = float(input("Gib den Wert in Liter an: "))
        outputKubikdezi = inputLiter * umrechnungsfaktor1
        print(inputLiter,"Liter sind",outputKubikdezi,"dm³")
        outputKubikmeter = inputLiter / umrechnungsfaktor1000
        print(inputLiter,"Liter sind",outputKubikmeter,"m³")

# Umrechnung von Kubikdezimeter in Liter und Kubikmeter
    elif wahl == "kubikdezimeter":
        inputKubikdezi = float(input("Gib den Wert in Kubikdezimeter an: "))
        outputLiter = inputKubikdezi * umrechnungsfaktor1
        print(inputKubikdezi,"dm³ sind",outputLiter,"Liter")
        outputKubikmeter = inputKubikdezi / umrechnungsfaktor1000
        print(inputKubikdezi,"dm³ sind",outputKubikmeter,"m³")
    
# Umrechnung von Kubikmeter in Liter und Kubikdezimeter
    elif wahl == "kubikmeter":
        inputKubikmeter = float(input("Gib den Wert in Kubikmeter an: "))
        outputLiter = inputKubikmeter * umrechnungsfaktor1000
        print(inputKubikmeter,"m³ sind",outputLiter,"Liter")
        outputKubikdezimeter = inputKubikmeter * umrechnungsfaktor1000
        print(inputKubikmeter,"m³ sind",outputKubikdezimeter,"dm³")


# Sprung zum Anfang (while-Schleife)
    neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ").lower()
    if neueEingabe == "ja":
        eingabeJaNein = 1
    elif neueEingabe == "nein":
        eingabeJaNein = 0
