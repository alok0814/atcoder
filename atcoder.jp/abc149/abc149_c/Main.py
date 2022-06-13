x = int(input())
prime = 0
if x == 2:
  prime = 2
else:
  for i in range(x, 10**6):
    flag = False
    for j in range(2, i):
      if i % j == 0: 
        flag = True
        break
    if flag == False: 
      prime =i
      break
print(prime)