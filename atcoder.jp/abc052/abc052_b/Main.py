n = int(input())
s = list(input())
x = 0
M = 0
for i in range(n):
  if s[i] == "I": x += 1
  elif s[i] == "D": x -= 1
  M = max(M, x)
print(M)


