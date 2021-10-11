l = list(map(int, input().split()))
count = 0

while l[count] % 2 == 0:
    count += 1

for i in range(count + 1, len(l)):
    if l[i] < l[count] and l[i] % 2 != 0:
        count = i

print(l[count])
