# Der folgende Code beschreibt, wie im Museum die Eintrittspreise berechnet werden.

# Erkläre in deutscher Sprache, wie sich der Preis berechnet.

# Was passiert, wenn man die Variable vereinsmitglied = False setzt?

# alter = 65
# vereinsmitglied = True

# preis = 6

# if alter > 55 or alter < 5:
#     preis = preis / 2
    
# if vereinsmitglied:
#     preis = 0

# print(f"Ihr Preis ist {preis}")

# Der Grundpreis beträgt 6 €. Wenn die Person älter als 55 ist oder jünger als 5, halbiert sich der Preis. Vereinsmitglieder zahlen unabhängig vom Alter 0 €.

alter = 65
vereinsmitglied = False

preis = 6

if alter > 55 or alter < 5:
    preis = preis / 2
    
if vereinsmitglied:
    preis = 0

print(f"Ihr Preis ist {preis}")

# Ihr Preis ist 3. 