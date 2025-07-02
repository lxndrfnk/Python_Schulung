# Im Folgenden wurde eine Klasse Person mit den Methoden __init__ und fullname erstellt. 
# Diese soll nun erweitert werden: 
# Da es sein kann, dass Personen gewisse Titel wie "Dr". oder "Prof." haben, sollen diese in unserer Klasse mit aufgenommen werden. 
# Es wurde bereits der Parameter title hinzugefügt, allerdings noch nicht als Instanzattribut. 
# Weiterhin soll bei der Ausgabe vom ganzen Namen, der Title vorweg mit ausgegeben werden. 
# Passe die Methode fullname dementsprechend an. 
# (Optional:) Passe die Methode fullname soweit an, dass immer ein Punkt nach dem Titel ausgegeben wird, auch wenn bspw. title="Dr" ist.

class Person():

    def __init__(self, firstname, lastname, title):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title

    def fullname(self):
        return self.title + "." + " " + self.firstname + " " + self.lastname
    
    
  
person_1 = Person("John", "Dorian", "Dr")
person_2 = Person("Perry", "Cox", "Dr")

print(person_1.fullname())
print(person_2.fullname())
