# a)

# Erstelle eine Funktion is_prime(n), die überprüft, ob eine Zahl n > 0 eine Primzahl ist. 
# Eine Primzahl ist eine positive, ganze Zahl, die genau durch zwei Zahlen (1 und sich selbst) ohne Rest teilbar ist. 
# So ist z.B. 5 eine Primzahl, aber 4 nicht, da 4 durch 1, 2 und 4 ohne Rest geteilt werden kann und damit drei Teiler hat. 
# Die 1 ist dabei keine Primzahl, da sie nur einen einzigen Teiler hat und keine zwei.

# Hier sind Unittests für dich, mit denen du deine Funktion prüfen kannst:

# def is_prime(n):
#     if n < 2:
#         return False

#     for teiler in range(2, n):
#         if n % teiler == 0:
#             return False
    
#     return True

# print(is_prime(12))

# import unittest

# class TestIsPrime(unittest.TestCase):
#     def test_prime(self):
#         self.assertTrue(is_prime(2))
#         self.assertTrue(is_prime(3))
#         self.assertTrue(is_prime(5))
#         self.assertTrue(is_prime(7))
#         self.assertTrue(is_prime(11))

#     def test_not_prime(self):
#         self.assertFalse(is_prime(1))
#         self.assertFalse(is_prime(4))
#         self.assertFalse(is_prime(6))
#         self.assertFalse(is_prime(8))
#         self.assertFalse(is_prime(9))
#         self.assertFalse(is_prime(10))

# if __name__ == '__main__':
#     unittest.main()

# b)

# Erstelle eine Funktion primes_up_to(n), die alle Primzahlen von 1 bis zur Zahl n (inklusive) berechnet und als Liste zurückgibt. 
# Verwende dabei die Funktion is_prime(n). Auch hier findest du Unittests zur Überprüfung deiner Funktion:

def is_prime(n):
    if n < 2:
        return False

    for teiler in range(2, n):
        if n % teiler == 0:
            return False
    
    return True

def primes_up_to(n):
    return [zahl for zahl in range(2, n + 1) if is_prime(zahl)]

print(primes_up_to(12))

