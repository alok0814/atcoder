n, x = map(int, input().split())
a = list(map(int, input().split()))
happy = 0
a.sort()
for i in range(n):
  if x < a[i] or (x != a[i] and i == n-1) : break
  x -= a[i]
  happy += 1
print(happy)