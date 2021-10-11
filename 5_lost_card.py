n = int(input())
sum = 0
sum_of_all = 0

for i in range(1, n):
    a = int(input())
    sum_of_all += i
    sum += a

sum_of_all += n
print(sum_of_all - sum)
