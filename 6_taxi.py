n = list(map(int, input().split()))
m = list(map(int, input().split()))
sum = 0

n.sort()
m.sort(reverse=True)

for i in range(len(n)):
    sum += n[i] * m[i]

print(sum)
