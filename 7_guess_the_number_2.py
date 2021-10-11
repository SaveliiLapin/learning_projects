line = ''
n = int(input())
l = set(range(1, n + 1))

while line != 'HELP':
    line = input()
    if line != 'HELP':
        line = set(map(int, line.split()))

        if 2 * len(l & line) <= len(l):
            print('NO')
            l -= line
        elif 2 * len(l & line) > len(l):
            print('YES')
            l &= line

print(*sorted(l))
