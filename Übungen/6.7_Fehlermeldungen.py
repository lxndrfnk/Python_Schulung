# Im Folgenden wurde eine Klasse Car erstellt. 
# Was genau __init__ und self hierbei machen werden wir uns später noch anschauen. 
# Wir können sehen, dass einige Instanzattribute hinzugefügt wurden: die Marke, die Farbe und die Anzahl an Türen. 
# Versuche vorherzusagen welche print Ausgabe zu einer Fehlermeldung führt und welche nicht. Teste sie einzelnd!

class Car():
    def __init__(self, brand, color, door_num):
        self.brand = brand
        self.color = color
        self.door_num = door_num

car = Car("VW", "black", 4)

# Tests

# print(car.brand()) # Fehler
# print(car.color) # kein Fehler
# print(Car.door_num) # Fehler
print(car.model) # Fehler
