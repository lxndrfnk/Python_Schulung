# Im Folgenden wurde eine Klasse Person mit den Methoden __init__ und fullname erstellt. Diese soll nun erweitert werden!

# Aufgabe 1: Es soll eine Methode shortname() hinzugefügt werden, die den vollständigen Namen in der Form "Dr. M. Mustermann" ausgibt. 
# D.h. anführend der Titel, anschließend der erste Buchstabe des Vornamens mit Punkt und zuletzt der vollständige Nachname.

# Aufgabe 2: Es soll eine Methode bmi() hinzugefügt werden, die den Body Mass Index berechnet. Dieser berechnet sich allgemein aus Gewicht geteilt durch die quadrierte Körpergröße.

# Aufgabe 3: Es soll eine Methode age() hinzugefügt werden, die das aktuelle Alter ausgibt. 
# Wir wollen die berechnung hierfür einfach halten und davon ausgehen, dass im aktuellen Jahr bereits jeder Geburtstag hatte, heißt: 
# Ist jemand im letzten Jahr geboren, ist er für unsere Methode automatisch ein Jahr alt. 
# Baue zusätzlich eine Abfrage ein, falls das Geburtsdatum in der Zukunft liegt. Für diesen Fall soll "not yet born" zurückgegeben werden

# Wichtiger Hinweis: Derzeit haben wir noch nicht gelernt, wie wir selbst Exceptions werfen, 
# daher geben wir uns hier damit zufrieden im Fehlerfall einen String zurückzugeben. Normalerweise sollte man hier eine Exception werfen!

class Person():

    def __init__(self, firstname, lastname, birthyear, weight, bodysize, title=""):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.weight = weight
        self.bodysize = bodysize
        self.title = title
   
    def fullname(self):
        return self.title + " " + self.firstname + " " + self.lastname
    
# shortname()

    def shortname(self):
        return self.title + " " + self.firstname[0] + ". " + self.lastname

# bmi()

    # def bmi(self):
    #     return self.weight/(self.bodysize ** 2)

# age()

    # def age(self):
    #     if 2025 - self.birthyear > 0:
    #         return 2025 - self.birthyear
    #     else:
    #         return "not yet born"
    
# Testpersonen
person_1 = Person("James", "Kirk", 2233, 77, 1.77, "Captain")
person_2 = Person("William", "Shatner", 1931, 106, 1.77)

# Test
print(person_1.shortname())     # Captain J. Kirk
print(person_2.shortname())     # W. Shatner

# print(person_1.bmi())           # 24.5778...
# print(person_2.bmi())           # 33.8344...

# print(person_1.age())           # not yet born
# print(person_2.age())           # 94
