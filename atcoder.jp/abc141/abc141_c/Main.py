n,k,q = map(int, input().split())
scr = [k]*n

for i in range(q):
	scr[int(input())-1] += 1
for s in scr:
  if s > q : print("Yes")
  else : print("No")