# Die folgende Funktion berechnet das Marsgewicht für eine einzelne Variable:

# gewicht = 65
# mars_faktor = 0.38
# mars_gewicht = gewicht * mars_faktor
# print(f'Dein Marsgewicht: {mars_gewicht}')

# a) Passe das Programm so an, dass für eine Liste gewichte = [100, 65, 23] die Berechnung durchgeführt wird und auf der Konsole erscheint:

# gewichte_erde = [100, 65, 23]
# mars_faktor = 0.38

# for e in gewichte_erde:
#     gewichte_mars = e * mars_faktor
#     print(f"Dein Marsgewicht: {gewichte_mars}.")

# b) Erweitere das Programm, sodass zusätzlich alle Marsgewichte in einer Liste gespeichert und am Ende ausgegeben werden.

gewichte_erde = [100, 65, 23]
mars_faktor = 0.38
gewichte_mars = []


for e in gewichte_erde:
    gewicht_mars = e * mars_faktor
    gewichte_mars.append(gewicht_mars)
    print(f"Dein Marsgewicht: {gewicht_mars}.")
print(f"Marsgewichte: {gewichte_mars}.")
    