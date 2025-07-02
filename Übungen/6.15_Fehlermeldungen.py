# Im Folgenden wurde eine Klasse Person mit den Methoden __init__ und fullname erstellt.

class Person():
  
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        return self.firstname + " " + self.lastname

# Dieser Code lässt sich ohne Fehlermeldung ausführen, allerdings erscheint eine Fehlermeldung sobald versucht wird eine Instanz zu erzeugen:

person = Person("Luke", "Skywalker")

print(person.fullname())


