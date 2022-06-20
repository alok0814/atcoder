n = int(input())
p = list(map(int,input().split()))
m = p[0]
cnt = 0
for i in p:
  if i <= m : cnt += 1
  m = min(m, i)
print(cnt)
