# Im folgenden ist die Funktion rechteck_umfang gegeben.

# a) Welche der anschließenden Aufrufe führen zu einer Fehlermeldung? Führe sie nacheinander aus!

# def rechteck_umfang(a, b):
#     return 2 * (a + b)

# print(rechteck_umfang(1,2)) # 6

# print(rechteck_umfang(7.0,2)) # 18

# print(rechteck_umfang(3)) # rechteck_umfang() missing 1 required positional argument: 'b'

# print(rechteck_umfang(3,4,5)) # rechteck_umfang() takes 2 positional arguments but 3 were given

# b) Es wird eine kleine Änderung an der Funktion vorgenommen.

# Welche Aufrufe führen nun zu Fehlermeldungen? Finde eine Erklärung hierfür!

# def rechteck_umfang(a, b=2):
#     return 2 * (a + b)

# print(rechteck_umfang(1, 2)) # kein Fehler

# print(rechteck_umfang(7.0, 2)) # kein Fehler

# print(rechteck_umfang(3)) # kein Fehler

# print(rechteck_umfang(3, 4, 5)) # rechteck_umfang() takes from 1 to 2 positional arguments but 3 were given