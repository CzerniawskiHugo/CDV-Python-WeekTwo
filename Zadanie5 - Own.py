print('Ten program wylicza silnie')

def silnia(n):
    wynik = 1
    for i in range (1, n+1):
        wynik = wynik * i
    return wynik


print(silnia(4))