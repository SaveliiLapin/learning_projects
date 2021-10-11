s, n = map(int, input().split())
users = []
space = s
num = 0

for i in range(n):
    users.append(int(input()))
users.sort()

while num < len(users) and space > 0:
    space -= users[num]
    num += 1

if space < 0:
    num -= 1

print(num)
