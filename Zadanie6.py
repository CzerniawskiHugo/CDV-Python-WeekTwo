print('This app calculates the Newton equation n to k')

def factorial(n):
    res = 1
    for i in range(res, n + 1):
        res = res * i
    return res

def newt(n, k):
    return factorial(n)/ (factorial(k) * factorial(n - k))

n = int(input('Please provide argument n : '))
k = int(input('Please provide argument k : '))


print(newt(n, k))