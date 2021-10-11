fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
mass = [0] * 100
max = 0

for line in fin:
    student = line.split()
    mass[int(student[2]) - 1] += 1

for i in mass:
    if i > max:
        max = i

for i in range(len(mass)):
    if mass[i] == max:
        print(i + 1, end=' ', file=fout)

fin.close()
fout.close()
