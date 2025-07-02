# Bisher haben wir uns mit dem einfachsten Fall einer Klasse beschäftigt und auch einige solcher Klassen erstellt. 
# Jetzt wollen wir einen Schritt weiter gehen und unseren Objekten gewisse Eigenschaften geben.

# Als allererstes Beispiel hatten wir die Klasse Car:

class Car():
    pass

# Diese soll für uns eine Blaupause für Autos sein. 
# Um im ersten Anlauf einige Autos unterscheiden zu können, fügen wir der Klasse sogenannte Instanzattribute für die Eigenschaften Marke, Farbe und Türanzahl hinzu.

# Dies könnte im Anschluss folgendermaßen aussehen:

class Car():
    def __init__(self, marke, farbe, türanzahl):
        self.marke = marke
        self.farbe = farbe
        self.türanzahl = türanzahl

car_1 = Car("Audi", "schwarz", 5)
car_1.marke = "Opel"
car_1.türanzahl = 4
print(car_1.marke)
print(car_1.farbe)
print(car_1.türanzahl)

# class Car():
    
#     def __init__(self, brand, color, door_num):
#         self.brand = brand          
#         self.color = color          
#         self.door_num = door_num    

