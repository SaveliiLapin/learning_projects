n = int(input())

print('+___ ' * n)
for i in range(n):
    print('|', i + 1, ' / ', end='', sep='')
print()
print('|__\ ' * n)
print('|    ' * n)
