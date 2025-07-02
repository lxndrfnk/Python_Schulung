# Sag voraus, was bei Ausführung des Programms auf der Konsole ausgegeben wird.

# Was passiert, wenn alter = 15 ist?

# Was passiert, wenn alter = 15 und film_genre = "Märchen" ist?

# alter = 15
# film_genre = "Horror"

# if film_genre == "Horror": # True -> Deswegen wird der eingerückte if-Block als nächstes überprüft.
#     print("Wie alt bist du denn?")
  
#     if alter >= 18: # False
#         print("Viel Spaß beim Film!")
  
#     if alter < 18: # True
#         print("Das wird nichts!")

# print("Tschüss!")

alter = 15
film_genre = "Märchen"

if film_genre == "Horror": # False -> Deswegen wird der eingerückte if-Block NICHT überprüft.
    print("Wie alt bist du denn?")
  
    if alter >= 18: # False
        print("Viel Spaß beim Film!")
  
    if alter < 18: # True
        print("Das wird nichts!")

print("Tschüss!")

