print('This app prints reversed string...')
str = input('Please insert the string: ')

str2 = ''

for ch in range(0, len(str)):
    print(str[len(str)-1-ch])

print('The string to reverse is:' + str)
print('The reversed string is: ' + str2)