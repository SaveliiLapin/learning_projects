def CountSort(a):
    s = [0] * 101

    for i in a:
        s[i] += 1

    a = []

    for i in range(len(s)):
        for j in range(s[i]):
            a.append(i)

    return a


l = list(map(int, input().split()))
l = CountSort(l)

print(*l)
