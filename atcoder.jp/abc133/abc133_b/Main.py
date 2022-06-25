import math
n, d = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n-1):
  for j in range(i+1, n):
    sum = 0
    for k in range(d):
      sum += (l[i][k]-l[j][k])**2
    ans = math.sqrt(sum)
    if ans == ans // 1: cnt += 1
print(cnt)