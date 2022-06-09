N = int(input())
X = list(map(int, input().split()))
ans = max(X)**max(X)
for j in range(min(X), max(X)+1):
  sum = 0
  for i in range(N):
    sum += (X[i] - j)**2
  ans = min(ans, sum)
print(ans)