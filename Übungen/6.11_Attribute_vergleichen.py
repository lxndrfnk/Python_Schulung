# Im Folgenden wurde eine Klasse Car erstellt. Was genau __init__ und self hierbei machen werden wir uns später noch anschauen. 
# Zudem sind bereits zwei Instanzen dieser Klasse erstellt, deren Instanzattribute im folgenden verglichen werden sollen. 
# Hierbei soll der Wahrheitsgehalt folgender Aussagen zu dem VW und dem Audi belegt, bzw. widerlegt werden

# Der VW kommt im Duden nach dem Audi
# Die Farbe vom Audi ist grün
# Der VW ist teurer als der Audi
# Der VW hat mehr Türen als der Audi
# Der VW wurde vor 2005 gebaut
# Der Kilometerstand vom Audi ist durch 100 teilbar

# Prüfe den Wahrheitsgehalt dieser Aussagen, in dem du die entsprechenden Attribute überprüfst und boolschen Werte (True oder False) ausgeben lässt.

class Car():

    def __init__(self, brand, color, door_num, price, year, mileage):
        self.brand = brand
        self.color = color
        self.door_num = door_num
        self.price = price
        self.year = year
        self.mileage = mileage

car_1 = Car("VW", "black", 4, 8000, 2006, 95286)
car_2 = Car("Audi", "red", 2, 13000, 2009, 87200)

# ==========

print(car_1.brand > car_2.brand) # Der VW kommt im Duden nach dem Audi

# ==========

if car_2.color == "grün":
    print(True)
else:
    print(False) # Die Farbe vom Audi ist grün

# ==========
    
print(car_2.color == "grün")    # Die Farbe vom Audi ist grün

# ==========

# if car_1.price > car_2.price:
#     print(True)
# else:
#     print(False) # Der VW ist teurer als der Audi

# if car_1.door_num > car_2.door_num:
#     print(True)
# else:
#     print(False) # Der VW hat mehr Türen als der Audi

# if car_1.year < 2005:
#     print(True)
# else:
#     print(False) # Der VW wurde vor 2005 gebaut

# if car_2.mileage % 100 == 0:
#     print(True)
# else:
#     print(False) # Der Kilometerstand vom Audi ist ein vielfaches von 100