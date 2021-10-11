s = input()
ss = s[::-1]

print(s[0:s.find('h') + 1], end='')
print(s[s.find('h') + 1:len(s) - ss.find('h') - 1] * 2, end='')
print(s[len(s) - ss.find('h') - 1:len(s)])
