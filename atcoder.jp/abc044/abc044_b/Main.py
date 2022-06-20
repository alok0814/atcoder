w = input()
#print("Yes" if all([w.count(i)%2==0 for i in set(w)]) else "No")
w_set = set(w)
cnt = 0
for W in w_set:
  if w.count(W) % 2 == 0: cnt += 1
if cnt == len(w_set):
  print("Yes")
else:
  print("No")

