l = list(map(int, input().split()))
x = int(input())
place = 0

while place < len(l) and l[place] >= x:
    place += 1

print(place + 1)
