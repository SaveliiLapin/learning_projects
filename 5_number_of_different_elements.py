l = list(map(int, input().split()))
count = 1

for i in range(1, len(l)):
    if l[i] != l[i - 1]:
        count += 1

print(count)
