n = int(input())
s = []
DD = {}

for i in range(n):
    s = input().split()

    for j in range(1, len(s)):
        DD[s[j]] = s[0]

n = int(input())

for i in range(n):
    s = input()
    print(DD[s])
