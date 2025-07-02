# Gegeben sei der folgende Code von Funktionen. 
# Kopiere den Code und setze einen Breakpoint in Zeile 1. 
# Führe ihn im Debugger aus und notiere, welche Zeilen durchlaufen werden. Notiere auch für jede Zeile, wie der Stack aussieht.

# (Die Zeilennummern stehen rechts vom Code.)

# a)

# def add(a, b):                         # 1
#     result = a + b                     # 2
#     print("Result:", result)           # 3
#     return result                      # 4

# def multiply(x, y):                    # 6
#     product = x * y                    # 7
#     print("Product:", product)         # 8
#     return product                     # 9

# def main():                            # 11
#     print("Start main")                # 12
#     sum_val = add(3, 4)                # 13
#     mult_val = multiply(sum_val, 2)    # 14
#     print("Final result:", mult_val)   # 15

# main()                                 # 17

# b)

# def square(n):                              # 1
#     return n * n                            # 2

# def sub_calculation(n):                     # 4
#     result = square(n) * square(n)          # 5
#     return result                           # 6

# def calculation(n):                         # 7
#     total = 0                               # 8
#     for i in range(1, n+1):                 # 9
#         total = total + sub_calculation(i)  # 10
#     return total                            # 11

# print(calculation(3))                       # 12

# c)

def factorial(n):                       # 1
    if n == 0:                          # 2
        return 1                        # 3
    else:                               # 4
        result = n * factorial(n - 1)   # 5
        return result                   # 6

result = factorial(3)                   # 8
print("Factorial of 3:", result )       # 9
