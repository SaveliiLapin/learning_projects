fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
n_c = [0, 0]
t_c = [0, 0]
e_c = [0, 0]

for line in fin:
    student = line.split()
    student[2] = int(student[2])
    student[3] = int(student[3])

    if student[2] == 9:
        n_c[0] += student[3]
        n_c[1] += 1
    elif student[2] == 10:
        t_c[0] += student[3]
        t_c[1] += 1
    else:
        e_c[0] += student[3]
        e_c[1] += 1

print(n_c[0] / n_c[1], t_c[0] / t_c[1], e_c[0] / e_c[1], file=fout)

fin.close()
fout.close()
