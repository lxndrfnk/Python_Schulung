# Im Folgenden wurde eine Klasse "Person" mit den Methoden __init__, fullname, shortname, bmi und age erstellt. Diese soll nun erweitert werden!

# Aufgabe 1:
# Es soll eine Methode weight_category hinzugefügt werden, die den bmi-Wert einer Gewichtskategorie zuordnet und ausgibt. 
# Man hat bei einem bmi-Wert von unter 18,5 Untergewicht. Ab 18,5 hat man Normalgewicht, ab 25 Übergewicht und ab 30 Adipositas. 
# Lass dementsprechd "Underweight", "Normal weight", "Overweight" und "Obesity" ausgeben. 
# Berücksichtige hierbei zudem, dass es bereits eine implementierte Methode bmi() gibt, die diesen ausgibt. 
# Nutze diese in deiner neuen Methode, anstatt den bmi neu auszurechnen.

# Aufgabe 2:
# Es soll eine Methode lifestage() hinzugefügt werden, die die aktuelle Lebensphase ausgibt. 
# Hierbei zählt man als Kind, sofern man jünger als 14 Jahre ist. Ab 14 Jahren zählt man als Jugendlicher, ab 18 als Erwachsener und ab 67 als Rentner. 
# Lass dementsprechend "child", "teenager", "adult" und "pensioner" ausgeben. 
# Berücksichtige hierbei genauso, dass es bereits eine implementierte Methode age() gibt, die das Alter ausgibt. 
# Nutze diese genau wie die Methode bmi() anstatt das Alter neu auszurechnen. 
# Beachte zudem, dass die Methode age() auch "not yet born" zurück geben kann. In diesem Fall soll auch lifestage() "not yet born" zurückgeben.

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
    
    def shortname(self):
        return self.title + " " + self.firstname[0] + ". " + self.lastname
    
    def bmi(self):
        return self.weight / self.bodysize ** 2
    
    def age(self):
        if self.birthyear <= 2025:
            return 2025 - self.birthyear
        else:
            return "not yet born"

# weight_category()

    def weigth_category(self):
        if self.bmi() < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi() < 25:
            return "Normal weigth"
        elif 25 <= self.bmi() < 30:
            return "Overweigth"
        elif self.bmi() >= 30:
            return "Obesity"

# lifestage()

    def lifestage(self):
        if self.age() < 14:
            return "child"
        elif 14 <= self.age() < 18:
            return "teenager"
        elif 18 <= self.age() < 67:
            return "adult"
        elif self.age() >= 67:
            return "pensioner"


person_1 = Person("James", "Kirk", 2233, 77, 1.77, "Captain")
person_2 = Person("William", "Shatner", 1931, 106, 1.77)
person_3 = Person("Chris", "Pine", 1980, 78, 1.84) 
# print(person_1.bmi())
# print(person_1.weigth_category())
# print(person_2.bmi())
# print(person_2.weigth_category())
# print(person_3.bmi())
# print(person_3.weigth_category())
# print(person_1.lifestage())
# print(person_2.lifestage())
# print(person_3.lifestage())
  
import unittest


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person_1 = Person("James", "Kirk", 2233, 77, 1.77, "Captain")
        self.person_2 = Person("William", "Shatner", 1931, 106, 1.77)
        self.person_3 = Person("Chris", "Pine", 1980, 78, 1.84)  
    def test_weight_category(self):
        self.assertEqual(self.person_1.weight_category(), "Normal weight")
        self.assertEqual(self.person_2.weight_category(), "Obesity")
        self.assertEqual(self.person_3.weight_category(), "Normal weight")  
    def test_lifestage(self):
        self.assertEqual(self.person_1.lifestage(), "not yet born")
        self.assertEqual(self.person_2.lifestage(), "pensioner")
        self.assertEqual(self.person_3.lifestage(), "adult")  
if __name__ == '__main__':
    unittest.main()