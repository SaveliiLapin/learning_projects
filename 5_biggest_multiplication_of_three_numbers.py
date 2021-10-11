l = list(map(int, input().split()))

if len(l) < 4:
    print(*l)
else:
    ll = l
    max_max = max(ll)
    ll.remove(max_max)
    max_previous = max(ll)
    ll.remove(max_previous)
    max_prev_prev = max(ll)
    ll.remove(max_prev_prev)
    min_min = min(ll)
    ll.remove(min_min)
    if len(ll) > 0:
        min_previous = min(ll)
    else:
        min_previous = max_prev_prev

    if max_prev_prev * max_previous * max_max >\
            max_max * min_previous * min_min:
        print(max_prev_prev, max_previous, max_max)
    else:
        print(max_max, min_previous, min_min)
