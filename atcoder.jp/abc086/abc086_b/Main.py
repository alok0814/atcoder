import math
a,b=map(str,input().split())
n = a + b
# N = int(n.replace(" ", ""))
# flag = False
# for i in range(1, 100):
#   if i*i == N : flag = True 
# if flag : print('Yes') 
# else : print('No')
r = math.sqrt(int(n))
if r == int(r) : print('Yes') 
else : print('No')

