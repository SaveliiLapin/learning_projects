l = list(map(int, input().split()))
count = 0

while l[count] <= 0:
    count += 1

for i in range(count + 1, len(l)):
    if 0 < l[i] < l[count]:
        count = i

print(l[count])
