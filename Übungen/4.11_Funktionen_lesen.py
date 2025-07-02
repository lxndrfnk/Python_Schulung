# Das folgende Programm berechnet einen Preis.

# Was erscheint hier auf der Konsole, wenn das Programm ausgeführt wird?

# Erkläre, wie sich der Preis berechnet.

def berechne_rabbatierten_preis(preis, wochentag, alter):
  rabatt = 0

  if wochentag == "Sonntag" or wochentag == "Samstag":
    rabatt = rabatt + 0.25

  if alter > 65 or alter < 6:
    rabatt = rabatt + 0.5

  return preis * (1 - rabatt)


basis_preis = 10
heute = "Montag"
alter_kunde = 70

end_preis = berechne_rabbatierten_preis(basis_preis, heute, alter_kunde)
print(end_preis)
