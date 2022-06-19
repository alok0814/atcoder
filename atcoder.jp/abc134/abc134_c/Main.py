n = int(input())
a = [int(input()) for _ in range(n)]
A = sorted(a, reverse=True)
for i in range(n):
  if a[i] == A[0]:print(A[1])
  else:print(A[0])
    
  

