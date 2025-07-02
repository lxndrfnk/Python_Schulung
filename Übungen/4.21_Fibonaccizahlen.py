# Fibonacci-Zahlen sind mit die bekanntesten Zahlen im Volksmund und entstanden bereits im 12. Jahrhundert.

# "Wie viele Kaninchenpaare entstehen in einem Jahr, wenn jedes Paar ab dem zweiten Monat ein neues Paar zur Welt bringt?"

# Zu dieser Überlegung kam Fibonacci (Leonardo von Pisa), wahrscheinlich inspiriert durch seinen Kontakt mit dem hindu-arabischen Zahlensystem, 
# welches einen Grundpfeiler unserer heutigen Mathematik bildet.

# Die Fibonaccizahlen berschreiben eine Zahlenfolge, wobei jede neue Zahl die Summe der beiden vorherigen Zahlen ist. Starten tut diese Summe mit zweimal der Zahl 1. Das heißt:

# fibonacci(1) = 1            # 1. Folgenglied und Startwert
# fibonacci(2) = 1            # 2. Folgenglied und Startwert
# fibonacci(3) = 1 + 1 = 2    # 3. Folgenglied
# fibonacci(4) = 1 + 2 = 3    # 4. Folgenglied
# fibonacci(5) = 2 + 3 = 5    # 5. Folgenglied
# fibonacci(6) = 3 + 5 = 8    # 6. Folgenglied
...
# Aufgabe:

# Es ist eine Liste an Zahlen gegeben:

# zahlen = [275, 233, 627, 68, 377, 35, 987, 21, 14, 199, 46, 144, 112, 420, 931, 610, 74, 34, 855, 26, 82, 518, 333, 13, 10, 55, 95, 52, 765, 89]

# Es sollen alle Fibonaccizahlen, die in dieser Liste enthalten sind, herausgefiltert und in einer separaten Liste ausgegeben werden. Gehe hierbei folgendermaßen vor:

# Schreibe eine Funktion fibonacci_test, der eine Zahl n übergeben wird. 
# Diese Funktion soll True ausgeben, wenn die Zahl n eine Fibonaccizahl ist, andernfalls soll die Funktion False ausgeben.
# Schreibe anschließend eine Funktion fibonacci_test_list, der eine Liste an Zahlen übergibt wird. 
# Diese Funktion soll durch die Liste iterieren und mithilfe der Funktion fibonacci_test überprüfen ob es sich um eine Fibonaccizahl handelt oder nicht. 
# Falls ja soll die Zahl der neuen Liste hinzugefügt werden.

def fibonacci_test(n):
    lst = [1,1]
    while True:
        if n > lst[-1]:
            lst.append(lst[-1] + lst[-2])
        else:
            return n == lst[-1]

def fionacci_list_test(lst):
    return [zahl for zahl in lst if fibonacci_test(zahl)]

zahlen = [275, 233, 627, 68, 377, 35, 987, 21, 14, 199, 46, 144, 112, 420, 931, 610, 74, 34, 855, 26, 82, 518, 333, 13, 10, 55, 95, 52, 765, 89]
print(fionacci_list_test(zahlen))
