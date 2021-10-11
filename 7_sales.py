fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
customers = {}

for line in fin:
    s = line.split()
    if s[0] not in customers:
        customers[s[0]] = {s[1]: int(s[2])}
    elif s[1] not in customers[s[0]]:
        customers[s[0]][s[1]] = int(s[2])
    else:
        customers[s[0]][s[1]] += int(s[2])

for i in sorted([i for i in customers]):
    print(i, ':', sep='', file=fout)

    for j in sorted([k for k in customers[i]]):
        print(j, customers[i][j], file=fout)

fin.close()
fout.close()
