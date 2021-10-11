fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
temp = str()
Vasya_num = fin.readline()

for i in Vasya_num:
    if i.isdigit():
        temp += i

if len(temp) == 7:
    temp = '8495' + temp

Vasya_num = temp

for line in fin:
    temp = str()
    for i in line:
        if i.isdigit():
            temp += i

    if len(temp) == 7:
        temp = Vasya_num[0] + '495' + temp
    elif temp[0] != Vasya_num[0]:
        temp = list(temp)
        temp[0] = Vasya_num[0]
        temp = ''.join(temp)

    if Vasya_num == temp:
        print('YES', file=fout)
    else:
        print('NO', file=fout)

fin.close()
fout.close()
