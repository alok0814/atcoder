x = [int(i) for i in input()]
print(max(sum(x),x[0]-1 + (len(x)-1)*9))