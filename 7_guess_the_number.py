line = ''
n = int(input())
l = set(range(1, n + 1))

while line != 'HELP':
    line = input()
    if line == 'YES':
        l &= k
    elif line == 'NO':
        l -= k
    elif line != 'HELP':
        k = set(map(int, line.split()))

print(*sorted(l))
