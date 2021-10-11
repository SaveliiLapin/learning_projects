l = list(map(int, input().split()))
num = 0
count = 0
now_count = 1

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[j] == l[i]:
            now_count += 1

    if now_count > count:
        num = l[i]
        count = now_count

    now_count = 1

print(num)
