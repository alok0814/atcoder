N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0

for i in range(N):
  A = list(map(int,input().split()))
  sum = C
  for j in range(M):
    sum += A[j] * B[j]
  if sum > 0 : 
    ans += 1
print(ans)