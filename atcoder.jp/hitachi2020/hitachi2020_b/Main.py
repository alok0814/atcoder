A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(M)]
tmp = 10**5
MIN = min(a) + min(b)
for x,y,c in lst:
  tmp = a[x-1] + b[y-1] - c
  MIN = min(tmp, MIN)
print(MIN)