def merge(aa, bb):
    cc = []
    p_1 = 0
    p_2 = 0

    for i in range(len(aa) + len(bb)):
        if p_2 == len(bb) or p_1 < len(aa) and aa[p_1] < bb[p_2]:
            cc.append(aa[p_1])
            p_1 += 1
        else:
            cc.append(bb[p_2])
            p_2 += 1

    return cc


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*merge(a, b))
