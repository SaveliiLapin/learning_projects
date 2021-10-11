fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
clas = [(0, 0)] * 3  # максимальный балл, предыдущий макс балл


for line in fin:
    student = line.split()
    student[2] = int(student[2])
    student[3] = int(student[3])

    if student[3] > clas[student[2] - 9][0]:
        clas[student[2] - 9] = (student[3], clas[student[2] - 9][0])
    elif student[3] > clas[student[2] - 9][1] and \
            student[3] != clas[student[2] - 9][0]:
        clas[student[2] - 9] = (clas[student[2] - 9][0], student[3])

print(clas[0][1], clas[1][1], clas[2][1], file=fout)

fin.close()
fout.close()
