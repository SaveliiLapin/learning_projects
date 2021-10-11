fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
mass = []

for line in fin:
    s = line.split()
    s.pop(2)
    mass.append(s)

mass.sort()

for i in range(len(mass)):
    print(*mass[i], file=fout)

fin.close()
fout.close()
