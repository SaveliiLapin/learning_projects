s = input()
num = 1
print(s[0], end='')

while num < len(s):
    print('*', s[num], sep='', end='')
    num += 1
