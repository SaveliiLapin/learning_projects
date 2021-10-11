l = list(map(int, input().split()))
k, C = map(int, input().split())

l.append(C)

for i in range(len(l) - 1, k, -1):
    l[i], l[i - 1] = l[i - 1], l[i]

print(*l)
