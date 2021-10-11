def interception(aa, bb):
    cc = []
    p_1 = 0
    p_2 = 0

    while p_1 < len(aa) and p_2 < len(bb):
        if aa[p_1] == bb[p_2]:
            cc.append(aa[p_1])
            p_1 += 1
            p_2 += 1
        elif aa[p_1] < bb[p_2]:
            p_1 += 1
        else:
            p_2 += 1

    return cc


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*interception(a, b))
