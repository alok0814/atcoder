import string
az = [chr(i) for i in range(97, 97+26)]
s = input()
flag = True
for i in az:
  if i not in s : 
    print(i)
    flag = False
    break
if flag: print("None")