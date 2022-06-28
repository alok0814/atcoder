n = int(input())
t = list(map(int, input().split()))
m = int(input())
j = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
  tmp = t.copy()
  tmp[j[i][0]-1] = j[i][1]
  print(sum(tmp))

