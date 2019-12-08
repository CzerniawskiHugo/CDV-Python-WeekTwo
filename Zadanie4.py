import numpy as np

print('This app calculates the average and standard deviation')

while 1==1:

    n = int(input('Please insert the amount of numbers: '))

    r = []



    for i in range(n):
        r.append(int(input('Type the  value of r: ')))
        mean = np.mean(r)
        standard = np.std(r)




    print('The average of typed digits is: ' + str(mean))
    print('The standard deviation is equal to: ' + str(standard))

    q = str(input('If you wish to continue press y: '))

    if q != 'y':
        break