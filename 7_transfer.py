a, b, x, y = map(int, input().split())
print(len(set(range(min(a, b), max(a, b) + 1)) &
          set(range(min(x, y), max(x, y) + 1))))
