n = int(input())
b = list(map(int, input().split()))
a = b[0]+b[-1]
for i in range(n-2):
  a += min(b[i], b[i+1])
print(a)