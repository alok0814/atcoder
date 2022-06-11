N = int(input())
ans = 1
for _ in range(N):
  if ans * 2 <= N : ans *= 2
print(ans)