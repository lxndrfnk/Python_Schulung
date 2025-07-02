# Erstelle eine Funktion fak(n), die ein int als Parameter n erwartet. fak(n) berechnet das Produkt der natürlichen Zahlen von 1 bis n. Beispiele:

def fak(n):
    result = 1
    for counter in range(1, n+1):
        result = result * counter
    return result 