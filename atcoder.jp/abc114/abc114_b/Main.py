s = input()
x = [str(a) for a in str(s)]
Min = int(s)
for i in range(0, len(x)-2):
  Min = min(Min,abs(753 - int(x[i]+x[i+1]+x[i+2])))
print(Min)