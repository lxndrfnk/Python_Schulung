# Schreibe mithilfe der for-Schleife ein Programm, das alle Elemente einer Liste miteinander multipliziert und dieses Produkt am Ende ausgibt.

factors = [1, 2, 3]
product = 1
for f in factors:
    product =  product * f

print(f"Das Produkt von {factors} ist {product}.")