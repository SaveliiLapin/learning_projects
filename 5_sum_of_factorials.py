n = int(input())
fact = 1
ans = 0

for i in range(1, n + 1):
    fact *= i
    ans += fact

print(ans)
