diction = {}
rev_diction = {}
n = int(input())

for i in range(n):
    k, l = input().split()
    diction[k] = l
    rev_diction[l] = k

k = input()

if k in diction:
    print(diction[k])
else:
    print(rev_diction[k])
