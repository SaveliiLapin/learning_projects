l = list(map(int, input().split()))
max = 0

for i in range(len(l)):
    if l[i] > l[max]:
        max = i

print(l[max], max)
