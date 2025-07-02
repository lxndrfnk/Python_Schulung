# Ersetze die ... im folgenden Code so, dass zunächst geprüft wird, ob die in alter gespeicherte Zahl kleiner als 18 ist und man dann eine Abfuhr erhält. 
# Danach soll geprüft werden, ob das alter größer oder gleich 18 ist und man reingelassen wird.

alter = int(input("Wie alt bist du?"))

if alter < 18:
    print("Dieser Film ist nichts für dich!")

if alter >= 18:
    print("Du darfst rein.")
