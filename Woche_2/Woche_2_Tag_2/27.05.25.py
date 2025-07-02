# def roboter_tanken(robo):
#     robo["Tank"] += 100

# roboter = {"Farbe": "Metallic", "Gewicht": 111, "Tank": 100}
# print(roboter)
# roboter_tanken(roboter)
# print(roboter)

# ==========

# class Roboter:
#     def __init__(self, farbe, ps):
#         self.farbe = farbe
#         self.ps = ps

# robo1 = Roboter("grün", 30)
# print(f"Farbe des Roboters 1: {robo1.farbe}")
# print(f"Leistung des ersten Roboters: {robo1.ps}")
# robo2 = Roboter("blau", 50)
# print(f"Farbe des Roboters 2: {robo2.farbe}")
# print(f"Leistung des zweiten Roboters: {robo2.ps}")

# ==========

class Person:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
    def fullname(self):
        return self.vorname + " " + self.nachname
p = Person("Michael", "Blarr")
p.nachname = "Glücklich"
print(p.fullname())
print(Person.fullname(p))