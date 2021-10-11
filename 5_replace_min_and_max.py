l = list(map(int, input().split()))
minn = l.index(min(l))
maxx = l.index(max(l))

l[minn], l[maxx] = l[maxx], l[minn]

print(*l)
