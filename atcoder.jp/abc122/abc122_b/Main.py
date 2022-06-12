S = list(input())
n = 0
tmp = 0
for s in S:
  if s in "ACGT":
    n += 1
  else: 
    tmp = max(n, tmp)
    n = 0
tmp = max(n, tmp)
print(tmp)