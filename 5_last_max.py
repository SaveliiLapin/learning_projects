l = list(map(int, input().split()))
ind = 0

for i in range(len(l)):
    if l[i] >= l[ind]:
        ind = i

print(l[ind], ind)
