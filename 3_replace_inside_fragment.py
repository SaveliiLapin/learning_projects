s = input()
print(s[0:s.find('h') + 1], end='')
print(s[s.find('h') + 1:s.rfind('h')].replace('h', 'H'), end='')
print(s[s.rfind('h'):len(s)])
