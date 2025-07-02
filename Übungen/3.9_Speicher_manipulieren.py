# Schreibe ein Programm, das in einer Liste die Zahlen von 0 bis 8 gespeichert hat. Ziel dieses Programms ist es nun die gespeicherten Zahlen durch Nutzereingaben zu manipulieren.

# Das Programm fragt dann den Nutzer nach einer Zahl zwischen 0 und 8. Es speichert diese Eingabe in der Variable namens pos.

# Das Programm fragt den Nutzer dann nach dem zu speichernden Text. Dieser Text wird nun in der Liste an der Postion pos gespeichert und der bisherige Wert wird überschrieben.

# Erweitere das Programm so, dass der Nutzer immer wieder abgefragt wird.

# Die Konsolenausgabe sollte dann wie folgt aussehen:

speicher = [0, 1, 2, 3, 4, 5, 6, 7, 8]

while True: # erzeugt eine Endlosschleife
    print(f"Bisheriger Speicher: {speicher}")
    pos = int(input("An welcher Stelle [0-8] soll gespeichert werden?"))
    eingabe = str(input("Was soll gespeichert werden?"))
    speicher[pos] = eingabe
    print(speicher)