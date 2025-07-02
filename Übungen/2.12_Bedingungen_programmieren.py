# Schreibe einen kleinen Python-Code, der den Eintrittspreis berechnet. Es gelten folgende Regeln:

# Personen unter 18 Jahren zahlen 5 €.
# Personen ab 65 Jahren zahlen 5 €.
# Alle anderen zahlen 10 €.
# Mitglieder eines Clubs erhalten 50 % Rabatt auf den Eintrittspreis.

alter = int(input("Wie alt bist du?"))
mitglied = True

preis = 5 if alter > 64 or alter < 18 else 10

if mitglied:
    preis = preis * 0.5

print(f"Bitte zahle {preis} €.")