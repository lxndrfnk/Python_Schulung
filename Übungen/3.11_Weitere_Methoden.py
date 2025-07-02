liste = [3, 1, 4, 1, 5, 9, 2, 6]

# ===== append: fügt einen Eintrag am Ende hinzu =====

# liste.append(7)
# print(liste)  # [3, 1, 4, 1, 5, 9, 2, 6, 7]

# ===== copy: erstellt eine flache Kopie =====

# kopie = liste.copy()
# print(kopie)  # [3, 1, 4, 1, 5, 9, 2, 6, 7]

# ===== clear: entfernt alle Elemente =====

# kopie = liste.copy()
# kopie.clear()
# print(kopie)  # []

# ===== count: zählt, wie oft der Wert 1 vorkommt =====

# anzahl = liste.count(1)
# print(anzahl)  # 2

# ===== extend: erweitert die Liste um mehrere Elemente =====

# liste.extend([8, 9])
# print(liste)  # [3, 1, 4, 1, 5, 9, 2, 6, 7, 8, 9]

# ===== index: findet den Index des ersten Vorkommens von 5 =====

# index_von_5 = liste.index(5)
# print(index_von_5)  # 4

# ===== insert: fügt 1 an Position 0 ein =====

# liste.insert(0, 1)
# print(liste)  # [1, 3, 1, 4, 1, 5, 9, 2, 6, 7, 8, 9]

# ===== pop: entfernt das letzte Element =====

# liste.pop()
# print(liste) # [3, 1, 4, 1, 5, 9, 2]

# ===== remove: entfernt das erste Vorkommen von 1 =====

# liste.remove(1)
# print(liste)  # [3, 4, 1, 5, 9, 2, 6]

# ===== sort: sortiert die Liste =====

liste.sort()
print(liste)  