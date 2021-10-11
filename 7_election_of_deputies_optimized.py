fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
deputes, sum, n_sum = [], 0, 0
# кортеж: название партии, количесво голосов,
# количество кандидатов, порядковый номер

for line in fin:
    deputes.append((' '.join(line.split()[:-1]), int(line.split()[-1]), 0, len(deputes) + 1))
    sum += deputes[-1][1]

for i in range(len(deputes)):
    deputes[i] = (deputes[i][0], deputes[i][1], deputes[i][1] / (sum / 450), deputes[i][3])
    n_sum += int(deputes[i][2])

deputes.sort(key=lambda x: (-1 * (x[2] % 1), x[1]))

for i in range(450 - n_sum):
    deputes[i] = (deputes[i][0], deputes[i][1], int(deputes[i][2]) + 1, deputes[i][3])

deputes.sort(key=lambda x: x[3])

for i in deputes:
    print(i[0], int(i[2]), file=fout)

fin.close()
fout.close()
