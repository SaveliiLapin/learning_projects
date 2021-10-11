fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
parties = []
votes = []
sum = 0

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
    parties[i] = (parties[i], votes.count(parties[i]))
    sum += parties[i][1]

for i in parties:
    if i[1] / sum * 100 >= 7:
        print(i[0], file=fout)

fin.close()
fout.close()
