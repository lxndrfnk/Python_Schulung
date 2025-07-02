# Ein Kalenderjahr hat bekanntlich 365 oder 366 Tage. Nach dem Gregorianischen Kalenderjahr hat ein Jahr genau 365,2425 Tage.

# Um diesen Unterschied zu beheben, hat man Schaltjahre eingeführt:

# Alle vier Jahre wird ein zusätzlicher Tag am 29. Februar eingefügt.
# Ausnahme: Jahre, die durch 100 teilbar sind, sind keine Schaltjahre.
# Ausnahme der Ausnahme: Jahre, die durch 400 teilbar sind, sind doch wieder Schaltjahre.
# Schreiben Sie ein Python-Programm, das berechnet, ob eine gegebene Jahreszahl ein Schaltjahr ist oder nicht.

# Um zu prüfen, ob eine Zahl ganzzahlig durch eine andere Zahl Teilbar ist, kann der Moduloperator % wie im folgenden Beispiel verwendet werden:

# zahl = 124

# if zahl % 4 == 0:
#     print(f"{zahl} ist durch 4 teilbar.")
# else:
#     print(f"4 ist kein Teiler von {zahl}.")

jahr = int(input("Bitte gib ein Kalenderjahr an: "))

if jahr < 0:
    print("Bitte überprüfe deine Eingabe!")
elif jahr % 4 == 0 and not jahr % 100 == 0:
    print(f"{jahr} ist ein Schaltjahr!")
else:
    print(f"{jahr} ist kein Schaltjahr")