fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
words = {}

for line in fin:
    s = line.split()

    for i in s:
        words[i] = words.get(i, 0) + 1

words = sorted(words, key=lambda x: (-words[x], x))

for i in words:
    print(i, file=fout)

fin.close()
fout.close()
