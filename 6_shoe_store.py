n = int(input())
a = list(map(int, input().split()))
a.sort()
number = 0
size = n

for i in range(len(a)):
    if a[i] >= size:
        number += 1
        size = a[i] + 3

print(number)
