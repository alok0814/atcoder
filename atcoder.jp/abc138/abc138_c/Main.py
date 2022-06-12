n = int(input())
a = list(map(int, input().split()))
a.sort()
sum = a[0]
for i in range(n):
  sum = (a[i] + sum) / 2
print(sum)


