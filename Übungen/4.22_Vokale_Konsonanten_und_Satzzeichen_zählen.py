# So ziemlich alle Wörter bestehen aus einer Kombination aus Vokalen und Konsonanten. 
# Bilden wir ganze Sätze und Texte, so kommen auch Satzzeichen hinzu.

# Es soll eine Funktion count_vocal_consonant_punctuation programmiert werden, 
# die einen string entgegennimmt und ein Dictionary, in dem gezählt wird, 
# wie viele Vokale, Konsonanten und Satzzeichen string enthält, zurück gibt.

# Hierzu sollen vorab zwei weitere Funktionen is_vocal und is_punctuation definiert werden, 
# die überprüfen sollen, ob ein einzelnes Zeichen jeweils ein Vokal oder Satzzeichen ist, und dementsprechend True oder False zurückgeben.

# Damit du dir keine Gedanken über die Satzzeichen machen musst kannst hierfür folgenden string übernehmen, 
# durch den du auch iterieren kannst: "!\"#$%\&'()*+,-./:;<=>?@[\\]^_{|}~"`

# Beispiel 1:

# Angenommenn wir haben den Satz "Hello World!". 
# Dieser Satz enthält 3 Vokale (das "e" und "o" aus "Hello", und das "o" aus "World"), 
# 7 Konsonanten ("H", "l", "l", "W", "r", "l", "d") und ein Satzzeichen ("!"). 
# Diese sollen durch die Funktion count_vocal_consonant_punctuation in einem Dictionary gezählt werden sodass wir folgende Ausgabe erhalten:

{'vocal': 3, 'consonant': 7, 'punctuation': 1}
