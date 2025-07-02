# Erstelle Code, der eine Lampe speichert mit den Eigentschaften: farbe, stromverbrauch, angeschaltet.

# a) Stelle die Lampe als Dictionary dar.

# lampe = {"farbe": "weiß", "stromverbrauch": 60, "angeschaltet": False}

# b) Stelle die Lampe als Klasse dar.

class Lampe():
    def __init__(self, farbe, stromverbrauch, angeschaltet=False):
        self.farbe = farbe
        self.stromverbrauch = stromverbrauch
        self.angeschaltet = angeschaltet
    
    def schalterstellung(self):
        return self.angeschaltet

lampe_1 = Lampe("rot", 80, False)
print(Lampe.schalterstellung(lampe_1))
print(lampe_1.farbe)

        
# Weiterhin soll eine Funktion/Methode einschalten und ausschalten erstellt werden, mit der angeschaltet jeweils auf True oder False gesetzt wird.

# a) Erstelle die Funktion für das Dictionary.

# b) Erstelle die Methode in der Klasse.

# Wie unterscheidet sich jeweils die Syntax (Art des Aufschreibens) bei diesen beiden Varianten?