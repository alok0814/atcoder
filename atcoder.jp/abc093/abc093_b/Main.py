a,b,k = map(int, input().split())
if a == b : print(a)
else:
  s = set()
  for i in range(min(k, b-a)):
    s.add(a+i)
    s.add(b-i)
  for a in sorted(s):print(a)