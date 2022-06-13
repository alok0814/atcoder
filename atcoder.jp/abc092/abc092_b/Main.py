n = int(input())
d, choco = map(int, input().split())
a = list(int(input()) for _ in range(n))
for i in range(len(a)):
  for j in range(0, d):
    if d >= j*a[i] + 1:
      choco += 1
    else:break
print(choco)