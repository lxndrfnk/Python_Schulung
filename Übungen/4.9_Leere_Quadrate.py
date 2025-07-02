# a) Lösung ohne Parameter:

def quadrat(n, symbol='*'):
    for i in range(n):
        for j in range(n):
            s = symbol if i in [0, n-1] or j in [0, n-1] else " "
            print(s, end="")
        print("\n")

# b) Lösung mit Parameter:

def quadrat(n, symbol='*', filled=True):
    for i in range(n):
        for j in range(n):
            s = symbol if filled or i in [0, n-1] or j in [0, n-1] else " "
            print(s, end="")
        print("\n")