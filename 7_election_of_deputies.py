fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
candidates = {}
candidates_s = []
ans = []
sum = 0
sum_s = 0

for line in fin:
    s = line.split()
    count = int(s[-1])
    s.pop()
    candidates[' '.join(s)] = count
    ans.append(' '.join(s))
    sum += count

for i in candidates:
    candidates_s.append((i, candidates[i] / (sum / 450)))
    sum_s += int(candidates_s[-1][1])

candidates_s.sort(key=lambda x: (-1 * (x[1] % 1), candidates[x[0]]))

for i in range(len(candidates_s)):
    if sum_s != 450:
        candidates_s[i] = (candidates_s[i][0], int(candidates_s[i][1]) + 1)
        sum_s += 1
    else:
        candidates_s[i] = (candidates_s[i][0], int(candidates_s[i][1]))

    temp, num = candidates_s[i]

    ans[ans.index(temp)] = (ans[ans.index(temp)], num)


for i in ans:
    print(i[0], i[1], file=fout)

fin.close()
fout.close()
