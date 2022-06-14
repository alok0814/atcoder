# x = [int(input())]
# i = 0
# while sum(x) != 0 :
#   if x[0] != 1:
#     x += [x[0]//2,x[0]//2] 
#   del x[0]
#   i += 1 
# print(i)
h = int(input())
x = 1
while x <= h:
  x*=2
print(x-1)