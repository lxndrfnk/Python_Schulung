# Erstelle eine Funktion quadrat(n), welches ein Quadrat aus Sternen zeichnet. Hier ein paar Beispiele:

def quadrat(n, symbol='*'):
    print(n * (n * symbol + "\n"))

quadrat(12, symbol='*')