n, m = map(int, input().split())
ann = set()
borya = set()

for i in range(n):
    ann.add(int(input()))

for i in range(m):
    borya.add(int(input()))

print(len(ann & borya))
print(*sorted(ann & borya))
print(len(ann - borya))
print(*sorted(ann - borya))
print(len(borya - ann))
print(*sorted(borya - ann))
