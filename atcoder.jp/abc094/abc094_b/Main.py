n, m, x = map(int, input().split())
A = list(map(int, input().split()))
cost = 0
if x < n // 2 :
  for i in range(x, 0, -1):
    for a in A:
      if i == a :
        cost +=1
else:
  for i in range(x, n+1):
    for a in A:
      if i == a :
        cost +=1
print(cost)