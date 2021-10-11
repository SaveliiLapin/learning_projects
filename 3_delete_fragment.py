s = input()
ss = s[::-1]

print(s[0:s.find('h')], end='')
print(s[len(s) - ss.find('h'):len(s)])
