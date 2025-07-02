# Erstelle eine Funktion counter(lst), die eine Liste lst als Parameter erwartet. 
# counter(lst) gibt ein Dictionary zurück, in dem für jeden Listeneintrag steht, wie oft er auftaucht.

# Hier sind drei Unittests, die die Funktionsweise von counter verdeutlichen:

def counter(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# Hier definierst du eine Liste:
meine_liste = ["Apfel", "Banane", "Apfel", "Zitrone"]

# Und hier rufst du die Funktion auf:
ergebnis = counter(meine_liste)

# Ausgabe zeigen:
print(ergebnis)

import unittest

class TestCounterBasic(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(counter([1, 2, 1, 3, 2, 1]), {1: 3, 2: 2, 3: 1})

    def test_strings(self):
        self.assertEqual(counter(["a", "b", "a", "c"]), {"a": 2, "b": 1, "c": 1})

    def test_mixed(self):
        self.assertEqual(counter([True, False, True, True]), {True: 3, False: 1})

if __name__ == '__main__':
    unittest.main()
