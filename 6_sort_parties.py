fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
parties = []
votes = []

for line in fin:
    line = line.rstrip()
    if line == 'PARTIES:':
        is_votes = 0
    elif line == 'VOTES:':
        is_votes = 1
    elif not is_votes:
        parties.append(line)
    else:
        votes.append(line)

for i in range(len(parties)):
    parties[i] = (votes.count(parties[i]), parties[i])

parties.sort(key=lambda x: (-x[0], x[1]))

for i in parties:
    print(i[1], file=fout)

fin.close()
fout.close()
