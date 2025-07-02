# Im Folgenden wurde eine Klasse Car erstellt. Was genau __init__ und self hierbei machen werden wir uns später noch anschauen. 
# Betrachte den folgenden Code und versuche vorherzusagen, was die Ausgaben der beiden print()-Befehle sein werden. 
# Finde im Anschluss eine Erklärung hierfür.

class Car():

    def __init__(self, brand, color, door_num):
        self.brand = brand
        self.color = color
        self.door_num = door_num

car_1 = Car("VW", "black", 4)
car_2 = Car("Audi", "red", 2)

car_1.model = "Golf"

print(car_1.model)
# print(car_2.model)
