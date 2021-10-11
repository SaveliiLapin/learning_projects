fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

s = fin.read()
s = set(s.split())

print(len(s), file=fout)

fin.close()
fout.close()
