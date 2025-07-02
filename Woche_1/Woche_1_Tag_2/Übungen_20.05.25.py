# ===== 2.2 Bedingung einfügen =====

# alter = int(input("Wie alt bist du?"))

# if alter < 18:
#     print("Dieser Film ist nichts für dich!")

# if alter >= 18:
#     print("Du darfst rein.")

# ===== 2.3 Einrückungsfehler =====

# alter = 17

# if alter > 18:
#     print("Du darfst Eintreten")

# else:
#     print("Tschüss")

# ===== 2.5 Bedingungen voraussagen 1 =====

# a = 3
# b = 5

# print(a > 5) # False
# print(b <= 5) # True
# print(a + b >= 5) # True
# print(a > b) # False
# print(a + 2 == b) # True   
# print(a) # 3
# print(b) # 5

# ===== 2.6 Bedingungen voraussagen 2 =====  

# preis = 3.50
# alter = 20 # alter = 20 => preis = 3.50

# if alter >= 65:
#     preis = preis - 2

# if alter < 7:
#     preis = 0.0

# print(f"Mit {alter} Jahren zahlst du: {preis} €.")

# preis = 3.50
# alter = 70 # alter = 70 => preis = 1.50

# if alter >= 65:
#     preis = preis - 2

# if alter < 7:
#     preis = 0.0

# print(f"Mit {alter} Jahren zahlst du: {preis} €.")

# preis = 3.50
# alter = 2 # alter = 2 => preis = 0.0

# if alter >= 65:
#     preis = preis - 2

# if alter < 7:
#     preis = 0.0

# print(f"Mit {alter} Jahren zahlst du: {preis} €.")

# ===== 2.7 Input voraussagen ===== 

# alter = int(input("Wie alt bist du?"))

# if alter < 0:
#     alter = 0

# print(f"Du bist {alter} Jahre alt.")

# ===== 2.8 Verschachtelte Bedingungen =====

# alter = 25
# film_genre = "Horror"

# if film_genre == "Horror":
#     print("Wie alt bist du denn?")
  
#     if alter >= 18:
#         print("Viel Spaß beim Film!")
  
#     if alter < 18:
#         print("Das wird nichts!")

# print("Tschüss!")

# alter = 15
# film_genre = "Horror"

# if film_genre == "Horror":
#     print("Wie alt bist du denn?")
  
#     if alter >= 18:
#         print("Viel Spaß beim Film!")
  
#     if alter < 18:
#         print("Das wird nichts!")

# print("Tschüss!")

# alter = 15
# film_genre = "Märchen"

# if film_genre == "Horror":
#     print("Wie alt bist du denn?")
  
#     if alter >= 18:
#         print("Viel Spaß beim Film!")
  
#     if alter < 18:
#         print("Das wird nichts!")

# print("Tschüss!")

# ===== 2.10 Bedingungen voraussagen 3 =====

# alter = 65
# vereinsmitglied = True

# preis = 6

# if alter > 55 or alter < 5:
#     preis = preis / 2
    
# if vereinsmitglied:
#     preis = 0

# print(f"Ihr Preis ist {preis}")

# ===== 2.11 Bedingungen voraussagen 4 =====

# name = "Thure"
# mitglied = True

# preis = 0
    
# if not mitglied:
#     preis = 3 

# if not "h" in name and not "H" in name:
#     preis = preis * 2

# print(f"{name} zahlt {preis} €.")

# Thure zahlt 0 €.

# name = "Henrik"
# mitglied = False

# preis = 0
    
# if not mitglied:
#     preis = 3 

# if not "h" in name and not "H" in name:
#     preis = preis * 2

# print(f"{name} zahlt {preis} €.")

# Henrik zahlt 3 €.

# name = "Emmi"
# mitglied = False

# preis = 0
    
# if not mitglied:
#     preis = 3 

# if not "h" in name and not "H" in name:
#     preis = preis * 2

# print(f"{name} zahlt {preis} €.")

# Emmi zahlt 6 €.

# ===== 2.12 Bedingungen programmieren =====

# alter = 30
# mitglied = True

# preis = 10

# if alter < 18 or alter > 64:
#     preis = 5

# if mitglied:
#     preis = preis / 2

# print (f"Du zahlst {preis} €.")

# ===== 2.13 Entweder ... oder =====

# briefmarke_alter = 25
# briefmarke_land = "Deutschland"

# if briefmarke_alter >= 20 or briefmarke_land == "Algerien":
#     print("Briefmarke kaufen!")
# else:
#     print("Briefmarke nicht kaufen.")

# briefmarke_alter = 20
# briefmarke_land = "Algerien"

# if (briefmarke_alter >= 20 or briefmarke_land == "Algerien") and not (briefmarke_alter >= 20 and briefmarke_land == "Algerien"):
#     print("Briefmarke kaufen!")
# else:
#     print("Briefmarke nicht kaufen!")

# ===== 2.15 Notenbewertung =====

# punktzahl = int(input("Wie viele Punkte hast du erhalten?"))

# if punktzahl >= 90 and punktzahl <= 100:
#     print("Sehr gut")
# elif punktzahl >= 80 and punktzahl <= 89:
#     print("Gut")
# elif punktzahl >= 70 and punktzahl <= 79:
#     print("Befriedigend")
# elif punktzahl >= 60 and punktzahl <= 69:
#     print("Ausreichend")
# elif punktzahl >= 101:
#     print("Überprüfe deine Eingabe!")
# else:
#     print("Ungenügend")

# ===== 2.16 Wochentagsbestimmung =====

# zahl = int(input("Gib eine Zahl zwischen 1 und 7 ein!"))

# if zahl == 1:
#     print("Montag")
# elif zahl == 2:
#     print("Dienstag")
# elif zahl == 3:
#     print("Mittwoch")
# elif zahl == 4:
#     print("Donnerstag")
# elif zahl == 5:
#     print("Freitag")
# elif zahl == 6:
#     print("Samstag")
# elif zahl == 7:
#     print("Sonntag")
# else:
#     print("Überprüfe deine Eingabe!")

# ===== 2.17 Fehlende Einrückungen =====

# alter = 20
# beschaeftigt = True

# if alter < 18:
#     print("Sie sind minderjährig.")
#     if beschaeftigt:
#         print("Es ist ungewöhnlich, in diesem Alter beschäftigt zu sein.")
#     else:
#         print("Genießen Sie Ihre Jugendzeit!")
# elif 18 <= alter < 65:
#     print("Sie sind im erwerbsfähigen Alter.")
#     if beschaeftigt:
#         print("Vielen Dank für Ihren Beitrag zur Gesellschaft.")
#     else:
#         print("Vielleicht sind Sie Student oder auf Jobsuche.")
# else:
#     print("Sie sind im Ruhestandsalter.")
#     if beschaeftigt:
#         print("Es ist beeindruckend, dass Sie noch arbeiten!")
#     else:
#         print("Genießen Sie Ihren wohlverdienten Ruhestand.")

# ===== 2.18 Syntaxfehler finden =====

# print("Willkommen zu deinem Abenteuer!")
# print("Du befindest dich an einer Kreuzung im Wald.")

# richtung = input("Möchtest du nach links oder rechts gehen? (links/rechts): ")

# if richtung == "links":
#     print("\nDu gehst nach links und siehst einen Fluss.")

#     aktion = input("Möchtest du den Fluss überqueren oder ihm folgen? (überqueren/folgen): ")

#     if aktion == "überqueren":
#         print("\nDu versuchst, den Fluss zu überqueren, aber die Strömung ist zu stark.")
#         print("Du wirst mitgerissen und das Abenteuer endet hier.")
#     elif aktion == "folgen":
#         print("\nDu folgst dem Fluss und findest ein kleines Dorf.")
#         print("Die Dorfbewohner heißen dich willkommen und bieten dir Unterkunft an.")
#         print("Herzlichen Glückwunsch! Du hast das Abenteuer erfolgreich abgeschlossen.")
#     else:
#         print("\nUngültige Eingabe. Das Abenteuer endet hier.")

# elif richtung == "rechts":
#     print("\nDu gehst nach rechts und stößt auf eine Höhle.")

#     aktion = input("Möchtest du die Höhle betreten oder vorbeigehen? (betreten/vorbeigehen): ")

#     if aktion == "betreten":
#         print("\nIn der Höhle findest du einen schlafenden Drachen.")

#         aktion2 = input("Möchtest du den Drachen wecken oder leise hinausgehen? (wecken/hinausgehen): ")
    
#         if aktion2 == "wecken":
#             print("\nDer Drache erwacht und ist verärgert über die Störung.")
#             print("Du wirst vom Drachen vertrieben und das Abenteuer endet hier.")
#         elif aktion2 == "hinausgehen":
#             print("\nDu verlässt leise die Höhle und setzt dein Abenteuer fort.")
#             print("Nach einiger Zeit findest du einen verborgenen Schatz.")
#             print("Herzlichen Glückwunsch! Du hast das Abenteuer erfolgreich abgeschlossen.")
#         else:
#             print("\nUngültige Eingabe. Das Abenteuer endet hier.")
    
#     elif aktion == "vorbeigehen":
#         print("\nDu gehst an der Höhle vorbei und gerätst in einen Hinterhalt von Räubern.")
#         print("Die Räuber nehmen all deine Habseligkeiten und das Abenteuer endet hier.")
#     else:
#         print("\nUngültige Eingabe. Das Abenteuer endet hier.")
# else:
#     print("\nUngültige Eingabe. Das Abenteuer endet hier.")

# ===== 2.19 Hundejahre berechnen =====

# alter_hund = int(input("Wie alt ist dein Hund?"))

# if alter_hund == 1:
#     print("Dein Hund ist in Menschenjahren 14 Jahre alt!")
# if alter_hund == 2:
#     print("Dein Hund ist in Menschenjahren 22 Jahre alt!")
# elif alter_hund >= 3:
#     alter_hund = alter_hund * 5
#     print(f"Dein Hund ist in Menschenjahren {alter_hund} Jahre alt!")

# age = int(input("Alter des Hundes: "))

# if age < 0:
#     print("Das stimmt wohl kaum!")
# elif age == 1:
#     print("entspricht ca. 14 Jahre")
# elif age == 2:
#     print("entspricht ca. 22 Jahre")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("Menschenjahre:", human)

# ===== 2.20 Schaltjahre berechnen =====

# zahl = int(input("Bitte gib eine Jahreszahl ein: "))

# if zahl % 4 == 0:
#     if zahl % 100 == 0:
#         if zahl % 400 == 0:
#             print(f"{zahl} ist ein Schaltjahr.")
#         else:
#             print(f"{zahl} ist kein Schaltjahr.")
#     else:
#         print(f"{zahl} ist ein Schaltjahr.")
# else:
#     print(f"{zahl} ist kein Schaltjahr.")

# ===== 2.21 Zeit um eine Sekunde erhöhen =====

# Eingabe: 12:59:59
# Ausgabe: 13:00:00

# Eingabe: 12:59:58
# Ausgabe: 12:59:59

# Eingabe: 23:59:59
# Ausgabe: 00:00:00

# stunden = int(input("Stunden: "))
# minuten = int(input("Minuten: "))
# sekunden = int(input("Sekunden: "))

# sekunden += 1

# if sekunden == 60:
#     sekunden = 0
#     minuten += 1
#     if minuten == 60:
#         minuten = 0
#         stunden += 1
#         if stunden == 24:
#             stunden = 0

# stunden = str(stunden).zfill(2)
# minuten = str(minuten).zfill(2)
# sekunden = str(sekunden).zfill(2)

# print(f"Neue Zeit: {stunden}:{minuten}:{sekunden}")

# ===== 2.24 if-else kürzen =====

# a)

# x = 7

# if x > 0:
#     result = "positiv"
# else:
#     result = "negativ oder null"

# print(f"{x} ist {result}.")

# x = -12

# result = "positiv" if x > 0 else "negativ oder null"

# print(f"{x} ist {result}.")

# b)

# gewicht = 50
# groesse = 180
# mitfahrerlaubnis = True

# if gewicht > 120 or groesse < 60:
#     mitfahrerlaubnis = False

# if mitfahrerlaubnis:
#     print(f"Du darfst mitfahren.")
# else:
#     print(f"Du darfst nicht mitfahren.")

# gewicht = 130
# groesse = 180
# mitfahrerlaubnis = True if gewicht < 120 and groesse > 60 else False

# if mitfahrerlaubnis:
#     print("Du darfst mitfahren.")
# else:
#     print("Du darfst nicht mitfahren.")

# c)

temp = 10

if temp < 0:
    feeling = "Gefroren"
elif 0 <= temp < 20:
    feeling = "Kalt"
elif 20 <= temp < 30:
    feeling = "Angenehm"
else:
    feeling = "Heiß"
