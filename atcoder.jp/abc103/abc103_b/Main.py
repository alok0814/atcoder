s = input()
t = input()
for i in range(len(t)):
  if s == t[i:] + t[:i] : 
    print("Yes")
    exit()
print("No")