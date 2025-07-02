# Richard hat einen Code geschrieben, der die Entscheidung trifft eine Briefmarke zu kaufen, wenn sie mindestens 20 Jahre alt ist oder wenn sie aus Algerien stammt oder beides.

# briefmarke_alter = 25
# briefmarke_land = "Deutschland"

# if briefmarke_alter >= 20 or briefmarke_land == "Algerien":
#     print("Briefmarke kaufen!")
# else:
#     print("Briefmarke nicht kaufen.")

# Nun möchte er den Code so anpassen, dass Briefmarken gekauft werden, wenn sie ENTWEDER mindestens 20 Jahre alt sind ODER aus Algerien kommen. 
# Wenn sie also mindestens 20 Jahre alt ist und aus Algerien, soll sie nicht gekauft werden. Hier ein paar Beispiele:

briefmarke_alter = int(input("Wie viele Jahre hat die Briefmarke schon auf dem Buckel?"))
briefmarke_land = str(input("Wo kommt die Briefmarke her?"))

if briefmarke_alter >= 20 and not briefmarke_land == "Algerien":
    print("Briefmarke kaufen.")
else:
    print("Briefmarke nicht kaufen.")

if briefmarke_land == "Algerien" and not briefmarke_alter <= 20:
    print("Briefmarke kaufen.")
else:
    print("Briefmarke nicht kaufen.")

    {}