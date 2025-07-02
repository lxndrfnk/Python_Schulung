# RANGE
# -----

# for number in range(3):
#     print(f"Das Doppelte von {number} ist {number * 2}")

# -----

# range(n) -> 0, 1, ..., n-1
# range(8) -> 0, 1, 2, 3, 4, 5, 6, 7

# -----

# for number in range(7, 15):
#     print(number)

# range(l, r) -> l, l+1,..., r-1
# range(7, 15) -> 7, 8, 9, 10, 11, 12, 13, 14


# for number in range(7, 15, 2):
#     print(number)

# range(l, r, s) -> l, l+s,..., r-1
# range(7, 15, 2) -> 7, 9, 11, 13

# -----

# ZWEI LISTEN PARALLEL DURCHLAUFEN
# -----

# waren = ["Apfel", "Birne", "Zitrone"]
# preise = [1, 1.2, 0.8]

# for ware, preis in zip(waren, preise):
#     print(f"Der Preis von {ware} ist {preis:.2f}€.")

# ===== SLICING =====

# numbers = [3, 2, 12, 54, 94, 2, -4, 22]

# print(numbers[2:5]) # [12, 54, 94]
# print(numbers[2:5:2]) # [12, 94]
# print(numbers[:5]) # [3, 2, 12, 54, 94]
# print(numbers[3:]) # [54, 94, 2, -4, 22] 
# print(numbers[:])  
# print(numbers[:-3]) # [3, 2, 12, 54, 94] 

# ===== LIST COMPREHENSION =====

# numbers = [1, 2, 3, 4] # ohne List Comprehension

# triple_numbers = []
# for number in numbers:
#     triple_numbers.append(number * 3)

# print(triple_numbers)

# -----

# numbers = [1, 2, 3, 4] # mit List Comprehension

# triple_numbers = [number * 3 for number in numbers] 

# print(triple_numbers)

# -----

# numbers = [3, 2, 12, 54, 94, 2, -4, 22] # mit List Comprehension
# print([n for n in numbers if n < 10])

# -----

# numbers = [3, 2, 12, 54, 94, 2, -4, 22] # ohne List Comprehension

# sizes = []
# for n in numbers:
#     sizes.append("klein" if n < 10 else "groß")

# print(sizes)

# -----

# numbers = [3, 2, 12, 54, 94, 2, -4, 22] # mit List Comprehension

# sizes = ["klein" if n < 10 else "groß" for n in numbers]

# print(sizes)

# ----- SET -> MENGE -----

# collection = {1, 2, 3, 2, 1, 4, 4, 5, 1, 2}
# print(collection) # {1, 2, 3, 4, 5}
# print(type(collection))

# ----- TUPLE -----

# collection = (1, 2, 3, 2, 1, 4, 4, 5, 1, 2)
# print(collection)
# print(type(collection))
# collection[1] = 5 # ⚡
# print(collection[-1])

# ----- DICTIONARY -----

# person = ["Hans", "Berlin", "Hausmeister", 34, "München"] # 'list'
# print(type(person))

# -----

# person = {
#     "Aufenthaltsort": "München",
#     "Name": "Hans",
#     "Geburtsort": "Berlin", 
#     "Beruf":"Hausmeister", 
#     "Alter": 10 + 20, 
#     }

# print(person["Name"]) # Hans
# person["Haarfarbe"] = "Schwarz"
# person["Alter"] = 50
# print(person["Haarfarbe"]) # Schwarz

# -----

person = {
    "Aufenthaltsort": "München",
    "Name": "Hans",
    "Geburtsort": "Berlin", 
    "Beruf":"Hausmeister", 
    "Alter": 10 + 20, 
    }

# for key, value in person.items():
#      print(f"Bei {key} steht {value}")

# for key in person:
#     print(key)

# for value in person.values():
#     print(value)