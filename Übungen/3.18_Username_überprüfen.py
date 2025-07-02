# In einem Onlineportal dürfen Nutzer ihren Benutzernamen frei wählen, jedoch gibt es bestimmte Begriffe, die nicht als Teil des Namens auftauchen dürfen. 
# Diese sind in der folgenden Liste verbotener Wörter notiert:

verboten = ['admin', 'super', 'user']

# Folgende Nutzernamen wären hier also verboten:

# superman
# administrator
# Radminister
# Häuser
# superadmin
# admin

# Schreibe ein Programm, das den Nutzer um einen Namen bittet und eine Warnmeldung gibt, wenn der Name verboten ist.

nutzername =input("Bitte gib deinen gewünschten Nutzernamen an: ")
nutzername_klein = nutzername.lower()

for v in verboten:
    if v in nutzername_klein:
        print("Diesen Namen darfst du leider nicht verwenden.")
    