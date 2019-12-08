
import math as m

print('This app prints the verse of Pascal triangle... ')

def equation(n, r):
    return int((m.factorial(n)) / ((m.factorial(r)) * m.factorial(n - r)))

def pascal(rows):
    res = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(equation(count, element))
        res.append(row)
    return res

rows = int(input(' Insert the number of rows: '))

for row in pascal(rows):
    print(row)