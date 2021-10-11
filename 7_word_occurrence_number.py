fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
words = {}

for line in fin:
    s = line.split()
    for i in s:
        if i not in words:
            print(0, end=' ', file=fout)
            words[i] = 1
        else:
            print(words[i], end=' ', file=fout)
            words[i] += 1


fin.close()
fout.close()
