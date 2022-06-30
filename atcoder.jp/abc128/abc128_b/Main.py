n = int(input())
l = []
for i in range(n):
  s,p = input().split()
  l.append([s,int(p)*(-1)])
t = sorted(l)
for T in t: print(l.index(T)+1)