# Schreibe eine Funktion alle_gleich(a, b, c), die drei Parameter annimmt und True zurückgibt, wenn alle gleich sind und False, wenn nicht.

# print(alle_gleich(1, 1, 1)) # True
# print(alle_gleich(3, 1 + 1 + 1, 5 - 2)) # True
# print(alle_gleich(1, 1, 2)) # False
# print(alle_gleich(3, 2, 1)) # False

# ===== Meine Lösung =====

def alle_gleich(a, b, c):
    if a == b == c:
        print(True)

alle_gleich(a=3, b=2, c=1)

# ===== Musterlösung =====

def alle_gleich(a, b, c):
  return a == b == c

print(alle_gleich(1, 1, 1)) # True
print(alle_gleich(3, 1 + 1 + 1, 5 - 2)) # True
print(alle_gleich(1, 1, 2)) # False
print(alle_gleich(3, 2, 1)) # False


