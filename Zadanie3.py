print('This app shows the sum of every number in a certain range...')


def suma(a, b):
    s = 0
    for n in range(a, b + 1):
        s = s + n
    return s



while 1==1:
    a = int(input('First digit: '))
    b = int(input('second digit: '))
    print(suma(a, b))
    q = str(input('If you wish to continue press y: '))
    if q != 'y':
        break