n = int(input())
l = list(map(int, input().split()))
x = int(input())

nearest = 0

for i in range(len(l)):
    if abs(x - l[i]) < abs(x - l[nearest]):
        nearest = i

print(l[nearest])
