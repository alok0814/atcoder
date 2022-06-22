n,a,b = map(int, input().split())
cnt = 0
for i in range(1, n+1):
  l = list(map(int, str(i)))
  if sum(l) >= a and sum(l) <= b: cnt += i
print(cnt)