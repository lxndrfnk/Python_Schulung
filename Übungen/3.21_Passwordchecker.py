# Schreibe ein Programm, das den Benutzer zur Eingabe eines Passworts auffordert. 
# Das Passwort muss bestimmte Kriterien erfüllen (z.B. mindestens 8 Zeichen lang, enthält sowohl Zahlen als auch Buchstaben). 
# Das Programm soll dem Benutzer mitteilen, ob das eingegebene Passwort gültig ist oder nicht. 
# Wenn das Passwort nicht gültig ist, soll das Programm spezifizieren, welche Kriterien nicht erfüllt wurden.

# Um zu prüfen, ob ein String eine Zahl ist, kann die Methode isdigit genutzt werden und um zu überprüfen, 
# ob ein String ein Buchstabe ist, kann isalpha genutzt werden:

password = input("Bitte gib ein Passwort ein: ")

# Prüfe, ob String lang genug ist
min_length_ok = len(password) >= 8

# Prüfe, ob wenigstens eine Zahl enthalten ist
digit_found = False
for char in password:
    if char.isdigit():
        digit_found = True
        break

# Prüfe, ob wenigstens ein Buchstabe enthalten ist
char_found = False
for char in password:
    if char.isalpha():
        char_found = True
        break
        
if min_length_ok and digit_found and char_found:
    print("Password ok 💚")
else:
    print("Password not ok 😰")