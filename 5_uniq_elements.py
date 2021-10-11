l = list(map(int, input().split()))

numbers = []
counts = []

for i in range(len(l)):
    if l[i] in numbers:
        counts[numbers.index(l[i])] += 1
    else:
        numbers.append(l[i])
        counts.append(1)

for i in range(len(numbers)):
    if counts[i] == 1:
        print(numbers[i], end=' ')
