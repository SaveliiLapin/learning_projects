l = list(map(int, input().split()))
pointer = 0

for i in range(len(l)):
    if l[i] != 0:
        l[i], l[pointer] = l[pointer], l[i]
        pointer += 1

print(*l)
