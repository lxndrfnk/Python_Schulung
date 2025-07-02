# Im Folgenden wurde eine Klasse Car erstellt. Was genau __init__ und self hierbei machen werden wir uns später noch anschauen. 
# Momentan hat die Klasse Car folgende Instanzattribute:

# brand (Marke)
# color (Farbe)
# door_num (Türenanzahl)
# price (Verkaufspreis)
# year (Baujahr)

# Es wurde zudem auch bereits eine Instanz dieser Klasse erzeugt, die nun erweitert werden soll.
# Der Instanz sollen nachträglich die Attribute discount und age hinzugefügt werden. 
# discount soll hierbei den Preis mit 10% Rabatt enthalten und age soll das aktuelle Alter angeben.

# Nutze für die Berechnung dieser bereits vorhandene Instanzattribute.

class Car():

    def __init__(self, brand, color, door_num, price, year, discount, age):
        self.brand = brand
        self.color = color
        self.door_num = door_num
        self.price = price
        self.year = year
        self.discount = price * 0.9
        self.age = 2025 - year

car = Car("VW", "black", 4, 8000, 2006, -1, -1)

# discount

# age

print(car.discount)           # 7200
print(car.age)                # 19
