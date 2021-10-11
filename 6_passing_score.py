fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
mass = []
max = (0, 0)  # максимальный балл, количество человек


k = int(fin.readline())

for i in fin:
    student = i.split()
    student[-3] = int(student[-3])
    student[-2] = int(student[-2])
    student[-1] = int(student[-1])

    if student[-3] >= 40 and student[-2] >= 40 and student[-1] >= 40:
        mass.append(student[-3] + student[-2] + student[-1])
        if mass[-1] > max[0]:
            max = (mass[-1], 1)
        elif mass[-1] == max[0]:
            max = (max[0], max[1] + 1)


if len(mass) <= k:
    print(0, file=fout)
elif max[1] > k:
    print(1, file=fout)
else:
    mass.sort(reverse=True)

    if mass.count(mass[k - 1]) > 1 and mass[k] == mass[k - 1]:
        print(mass[mass.index(mass[k - 1]) - 1], file=fout)
    else:
        print(mass[k - 1], file=fout)

fin.close()
fout.close()
