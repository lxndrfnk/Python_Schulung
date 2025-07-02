# Vielleicht ist dir schon aufgefallen, dass die Konsolenausgabe von Klassen sehr nichtssagend ist.
# Im folgenden Code findest du zwei Klassen, deren Instanzen auf der Konsole ausgegeben werden.
# Untersuche die beiden Konsolenausgaben und erkläre, wie sie zustande kommen.
# Passe dann die Konsolenausgabe von Peach so an, dass sie ebenfalls ihre Attribute ausgibt.

class Apple:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"Apple(name={self.name}, color={self.color})"


class Peach:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"Peach(name={self.name}, color={self.color})"

apple = Apple("Granny Smith", "Grün")
peach = Peach("Yellow Peach", "Gelb")

print(apple) 
print(peach)
