#before
# = int(input())
# a = [] 
# a.append(s)
# match = 0
# flag = False
# for i in range(0,10):
#   if a[i] % 2 == 0:
#     a.append(int(a[i]/2))
#   else:
#     a.append(int(3*a[i]+1))
# print(a)
# for i in range(0,1000000):
#   match = a[i]
#   for j in range(i+1,1000000):
#     if match == a[j]: 
#       match=j+1
#       flag = True
#       break
#   if flag: break
# print(match)
 
#after
s,S = int(input()),set()
for m in range(0,1000000):
  if s in S: break
  S.add(s)
  s = s//2 if s%2==0 else 3*s+1
print(m+1)