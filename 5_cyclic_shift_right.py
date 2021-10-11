l = list(map(int, input().split()))
x = l[0]

for i in range(1, len(l)):
    l[i], x = x, l[i]

l[0] = x

print(*l)
