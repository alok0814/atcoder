import math
a, b = map(int, input().split())
flag = True
for i in range(1, 10000):
  if math.floor(i*0.08) == a and math.floor(i*0.1) == b:
    print(i)
    flag = False
    break
if flag:print(-1)
    