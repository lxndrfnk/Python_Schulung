# name = "Aquafina"

# if "q" in name:
#     print("Das ist ja ein seltener Name!")

# print(f"Hallo {name}")

# alter = int(input("Wie alt bist du?"))

# if alter >= 18:
#     print("Du bist volljährig.") # Einrückung beachten
# else:
#     print("Du bist noch minderjährig.") # Einrückung beachten

# alter = 10
# name = "Holger"
 
# preis = 5
 
# if alter < 15:
#     preis = preis / 2
 
# if "o" in name:
#     preis = preis / 2
 
# print(preis)

alter = int(input("Wie alt bist du?"))
name = str(input("Wie heißt du?"))
 
preis = 5
 
if alter < 15:
    preis = preis / 2
    if "o" in name: # Die zweite Bedingung wird nur dann zusätzlich geprüft und ausgeführt, wenn die erste erfüllt ist
        preis = preis / 2
 
print(preis)