n = list(map(int, input().split()))
m = set()

for i in n:
    if i in m:
        print('YES')
    else:
        print('NO')
        m.add(i)
