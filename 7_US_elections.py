fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
diction = {}

for line in fin:
    name, num = line.split()
    num = int(num)
    diction[name] = diction.get(name, 0) + num

for i in sorted(diction):
    print(i, diction[i], file=fout)

fin.close()
fout.close()
