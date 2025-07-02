# Gegeben sei der folgende Code:

students = ["Anton", "Bernd", "Carlo", "Dennis", "Eva"]

# Was erscheint hier auf der Konsole? Erklären Sie jeweils, was sie sehen:

n = len(students) 

# print(f"Länge der Liste: {n}") # Länge der Liste: 5

# print(students[-1]) # Eva

# print(students[-2]) # Dennis

# print(students[-5]) # Anton

print(students[n-3]) # Carlo: hier gibt die Konsole das Element mit dem Index [n-3 = 2] aus. Also 