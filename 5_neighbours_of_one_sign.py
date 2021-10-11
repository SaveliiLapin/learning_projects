def one_sign(ll, countt):
    if ll[count] >= 0 and ll[count - 1] >= 0:
        return 0
    elif ll[count] < 0 and ll[count - 1] < 0:
        return 0
    else:
        return 1


l = list(map(int, input().split()))
count = 1

while count != len(l) and one_sign(l, count):
    count += 1

if count != len(l):
    print(l[count - 1], l[count])
