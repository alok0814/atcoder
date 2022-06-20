n, m = map(int,input().split())
l =  [list(map(int, input().split())) for _ in range(n)]
cnt = 0
L = []
for i in range(n):l[i].pop(0)
for i in l:
    for j in i:
        L.append(j)
for i in range(1,m+1):
  if L.count(i) == n: cnt += 1
print(cnt)