import itertools
n,m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
L = list(itertools.chain.from_iterable(l))
for i in range(1, n+1):
  print(L.count(i))