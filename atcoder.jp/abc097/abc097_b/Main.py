x = int(input())
m = 0
for i in range(1,min(x+1,33)):
  for j in range(2,min(10, x+2)):
    if i**j <= x:m = max(m,i**j)
print(m)