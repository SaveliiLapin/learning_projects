l = list(map(int, input().split()))

max_max = 0
max_previous = 0
min_min = 0
min_previous = 0

for i in l:
    if i >= max_max:
        max_previous = max_max
        max_max = i
    elif i > max_previous:
        max_previous = i

    if i <= min_min:
        min_previous = min_min
        min_min = i
    elif i < min_previous:
        min_previous = i

max_mult = max_max * max_previous
min_mult = min_min * min_previous
min_max = max_max * min_min

if max_mult > min_mult and max_mult > min_max:
    print(max_previous, max_max)
elif min_mult > max_mult and min_mult > min_max:
    print(min_min, min_previous)
else:
    print(min_min, max_max)
