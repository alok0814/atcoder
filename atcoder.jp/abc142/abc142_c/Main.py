n = int(input())
A = list(map(int, input().split()))
a = [0 for i in range(0, n)]
index = 0
for i in range(1, n+1):
  a[A[i-1] -1] = i
# a=[str(i) for i in a]
# a=' '.join(a)
print(*a)
