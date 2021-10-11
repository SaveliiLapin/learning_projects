n = int(input())
cities = list(map(int, input().split()))
m = int(input())
bombs = list(map(int, input().split()))
ans = []
p_2 = 0

for i in range(max(n, m)):
    if i < n:
        cities[i] = (cities[i], i + 1)
    if i < m:
        bombs[i] = (bombs[i], i + 1)

cities.sort()
bombs.sort()

for p_1 in range(n):
    if p_2 + 1 < m:
        while p_2 + 1 < m and abs(cities[p_1][0] - bombs[p_2][0]) > \
                abs(cities[p_1][0] - bombs[p_2 + 1][0]):
            p_2 += 1
    ans.append((cities[p_1][1], bombs[p_2][1]))

ans.sort()

for i in range(n):
    print(ans[i][1], end=' ')
