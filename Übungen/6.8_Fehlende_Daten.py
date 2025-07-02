# Im Folgenden wurde eine Klasse Car erstellt. Was genau __init__ und self hierbei machen werden wir uns später noch anschauen. 
# Desweiteren wurde bereits eine Instanz dieser Klasse erstellt, ein schwarzer VW mit 4 Türen. 
# Wir haben noch weitere Autos, die wir als Instanzen der Klasse Car darstellen wollen, jedoch sind einige dabei, wo wir nicht alle Daten haben. 
# Bspw. Haben wir einen roten Audi, bei dem der Eintrag der Türenanzahl fehlt. 
# Unser momentaner Code führt zu einer Fehlermeldung, da zur Erstellung einer Instanz alle Attribute gesetzt werden müssen. 
# Passe den Code soweit an, dass dieser einwandfrei funktioniert und keine Informationen verloren gehen. Hier ist etwas Kreativität gefragt!

class Car():

    def __init__(self, brand, color, door_num):
        self.brand = brand
        self.color = color
        self.door_num = door_num

car_1 = Car("VW", "black", 4)

car_2 = Car("VW", "red", -1)
