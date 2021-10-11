n, k = map(int, input().split())
ans = set()

for i in range(k):
    a, b = map(int, input().split())
    ans |= set(i for i in range(a, n + 1, b) if i % 7 != 0 and i % 7 != 6)

print(len(ans))
