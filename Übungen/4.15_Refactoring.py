# Jürgen nutzt den folgenden Code, um den Eintritt in seinen Eisenbahnpark zu berechnen:

# def berechne_preis(alter, mitglied):
#     if mitglied or alter < 4 or alter > 60:
#         return 0
#     if alter < 4:
#         return 0
#     if alter > 60:
#         return 0
#     return 2    

# Jürgen hat auch Tests geschrieben, um sicherzustellen, dass sein Code funktioniert:

# import unittest  

# class TestPreise(unittest.TestCase):
#     def test_berechne_preis_mitglied(self):
#         self.assertEqual(berechne_preis(20, True), 0)
        
#     def test_berechne_preis_kinder(self):
#         self.assertEqual(berechne_preis(2, False), 0)
        
#     def test_berechne_preis_retner(self):
#         self.assertEqual(berechne_preis(70, False), 0)
        
#     def test_berechne_preis_normal(self):
#         self.assertEqual(berechne_preis(20, False), 2)

# if __name__ == '__main__':
#     unittest.main()

# =====

# Alle seine Tests funktionieren.

# Jürgen hat nun kennengelernt, wie man Bedingungen mit or, and und not miteinander verknüpft und möchte nun seine Funktion etwas schlanker neu programmieren.

# Passe die Funktion von Jürgen an und achte dabei darauf, dass die Tests immer noch funktionieren!

def berechne_preis(alter, mitglied):
    if mitglied or alter < 4 or alter > 60:
        return 0
    else:
        return 2    

import unittest  

class TestPreise(unittest.TestCase):
    def test_berechne_preis_mitglied(self):
        self.assertEqual(berechne_preis(20, True), 0)
        
    def test_berechne_preis_kinder(self):
        self.assertEqual(berechne_preis(2, False), 0)
        
    def test_berechne_preis_retner(self):
        self.assertEqual(berechne_preis(70, False), 0)
        
    def test_berechne_preis_normal(self):
        self.assertEqual(berechne_preis(20, False), 2)

if __name__ == '__main__':
    unittest.main()