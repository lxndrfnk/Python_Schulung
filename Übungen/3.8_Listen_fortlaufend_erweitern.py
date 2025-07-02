# Schreibe ein Programm, das den Nutzer wiederholt nach einer Zahl fragt. 
# Das Programm hat intern eine Liste namens eingaben, in der alle bisher eingegebenen Zahlen gespeichert werden. 
# Es sollen vor der Eingabe immer die bisher gespeicherten Elemente eingeblendet werden.

eingaben = []
while True:
    print(f"Bisherige Zahlen: {eingaben}")
    eingabe = int(input("Gib eine Zahl ein: "))
    eingaben.append(eingabe)