n = int(input())
k = int(input())
all_know = set()
anyone_know = set()

for i in range(k):
    all_know.add(input())

anyone_know |= all_know

for i in range(n - 1):
    temp = set()
    k = int(input())
    for j in range(k):
        temp.add(input())
    anyone_know |= temp
    all_know &= temp

print(len(all_know))
print(*all_know, sep='\n')
print(len(anyone_know))
print(*anyone_know, sep='\n')
