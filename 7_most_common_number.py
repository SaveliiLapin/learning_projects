fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
diction = {}
rev_diction = {}

for line in fin:
    s = line.split()

    for i in s:
        diction[i] = diction.get(i, 0) + 1

for i in diction:
    if diction[i] not in rev_diction:
        rev_diction[diction[i]] = []
        rev_diction[diction[i]].append(i)
    else:
        rev_diction[diction[i]].append(i)

ss = sorted(rev_diction[sorted(rev_diction)[-1]])

print(ss[0], file=fout)

fin.close()
fout.close()
