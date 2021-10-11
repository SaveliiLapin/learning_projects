fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
candidates = {}
count = 0
max = ('', 0)  # имя кандидата, количество голосов
prev_max = ('', 0)

for line in fin:
    candidates[line.rstrip()] = candidates.get(line.rstrip(), 0) + 1
    count += 1

for i in candidates:
    if candidates[i] > max[1]:
        prev_max = max
        max = (i, candidates[i])
    elif candidates[i] > prev_max[1]:
        prev_max = (i, candidates[i])

if 2 * max[1] > count:
    print(max[0], file=fout)
else:
    print(max[0], prev_max[0], sep='\n', file=fout)

fin.close()
fout.close()
