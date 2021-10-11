s = input()
ss = s[::-1]

if s.find('f') != -1:
    if s.find('f') == len(s) - ss.find('f') - 1:
        print(s.find('f'))
    else:
        print(s.find('f'), len(s) - ss.find('f') - 1)
