n = int(input())
ans = []

for i in range(n):
    s = input().split()
    s[1] = int(s[1])
    ans.append((s[1], s[0]))

ans.sort(reverse=True)

for i in ans:
    print(i[1])
