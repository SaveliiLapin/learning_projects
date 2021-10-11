fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
nine = 0
ten = 0
eleven = 0

for line in fin:
    student = line.split()
    student[2] = int(student[2])
    student[3] = int(student[3])

    if student[2] == 9:
        if student[3] > nine:
            nine = student[3]
    elif student[2] == 10:
        if student[3] > ten:
            ten = student[3]
    else:
        if student[3] > eleven:
            eleven = student[3]

print(nine, ten, eleven, file=fout)

fin.close()
fout.close()
