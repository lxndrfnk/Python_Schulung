# Wir wollen eine Funktion entwickeln, die prüft, ob in einer Liste die Elemente an drei Positionen gleich sind. Der Methodenkopf sieht wie folgt aus:

def drei_gleich(liste, pos0, pos1, pos2):
    return liste[pos0] == liste[pos1] == liste[pos2]

import unittest  

class TestDreiGleich(unittest.TestCase):
    def test_drei_gleich_0(self):
        self.assertEqual(drei_gleich([1, 1, 1], 0, 1, 2), True)
        
    def test_drei_gleich_1(self):
        self.assertEqual(drei_gleich([1, 2, 1, 3, 1], 0, 2, 4), True)
        
    def test_drei_gleich_2(self):
        self.assertEqual(drei_gleich([1, 2, 1, 3, 1], 0, 1, 2), False)
        
    def test_drei_gleich_3(self):
        self.assertEqual(drei_gleich([1, 1, 2], 0, 1, 2), False)


if __name__ == '__main__':
    unittest.main()