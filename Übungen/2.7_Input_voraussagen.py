# Ersetze die ... in folgendem Programm so, dass eine Eingabe von negativen Zahlen (z.B. -100) vom Programm korrigiert wird. 
# Dazu soll zunächst geprüft werden, ob das eingegebene Alter negativ ist und wenn ja, soll dieses auf 0 gesetzt werden.

alter = int(input("Wie alt bist du?"))
if alter < 0:
    alter = 0

print(f"Du bist {alter} Jahre alt.")