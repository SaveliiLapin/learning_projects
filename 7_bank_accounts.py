fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
accounts = {}

for line in fin:
    s = line.split()

    if s[0] == 'BALANCE':
        if s[1] in accounts:
            print(accounts[s[1]], file=fout)
        else:
            print('ERROR', file=fout)
    elif s[0] == 'DEPOSIT':
        accounts[s[1]] = accounts.get(s[1], 0) + int(s[2])
    elif s[0] == 'WITHDRAW':
        accounts[s[1]] = accounts.get(s[1], 0) - int(s[2])
    elif s[0] == 'INCOME':
        for i in accounts:
            if accounts[i] > 0:
                accounts[i] = int(accounts[i] * (1 + int(s[1]) / 100))
    else:
        accounts[s[1]] = accounts.get(s[1], 0) - int(s[3])
        accounts[s[2]] = accounts.get(s[2], 0) + int(s[3])

fin.close()
fout.close()
