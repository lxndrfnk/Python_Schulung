# Mit if prüfe ich eine Bedingung:

# x = 10

# if x > 5:
#     print("x ist größer als 5")

# 👉 Wenn x > 5 wahr ist, wird der eingerückte Code („print…“) ausgeführt.

# In Python gehört alles, was eingerückt ist, zu dem if.

# Das ist wie ein Paket: Mit if starte ich das Paket – und die Einrückung zeigt, was alles dazugehört.

# x = 10

# if x > 5:
#     print("x ist größer als 5")
#     print("Das war ein Vergleich")  # Auch das gehört zum if-Block!

# 🚨 Wenn ich nicht einrücke, weiß Python nicht, was zu if gehört.

# -------------------- #

# elif ist eine weitere Bedingung, die geprüft wird, wenn die erste NICHT zutrifft.

# x = 5

# if x > 5:
#     print("x ist größer als 5")

# elif x == 5: # wird nur dann überprüft, wenn if x > 5 NICHT zutrifft
    # print("x ist genau 5")

# -------------------- #

# else wird immer zuletzt geprüft – und führt den Code aus, wenn keine der obigen Bedingungen zutrifft.

# x = 3

# if x > 5: # False
#     print("x ist groß")
# elif x == 5: # False
#     print("x ist mittel")
# else: # True
#     print("x ist klein")

# -------------------- #

temperatur = int(input("Wie warm ist es?"))
feuchtigkeit = int(input("Wie feucht ist es?"))

if temperatur > 30:
    print("Es ist heiß.")
if feuchtigkeit < 40:
        print("Die Luft ist trocken.")