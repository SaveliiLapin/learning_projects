def IsAscending(A):
    count = 1
    while count < len(A) and A[count] > A[count - 1]:
        count += 1
    return count


l = list(map(int, input().split()))

if IsAscending(l) != len(l):
    print('NO')
else:
    print('YES')
