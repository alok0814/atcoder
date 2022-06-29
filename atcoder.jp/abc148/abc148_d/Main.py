n, *a = map(int, open(0).read().split())
now = 0
for i in a:
  if i == now+1: now += 1
print(n-now if now else -1)
