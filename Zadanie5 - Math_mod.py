import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * math.factorial(n-1)





print('Ten program podaje silnie dla wybranego elementu. ')

n = int(input('Podaj element: '))

print(factorial(n))