s = input()
num = 0

while num < len(s):
    if num % 3 != 0:
        print(s[num], end='')
    num += 1
