h,w = map(int, input().split())
for _ in range(w+2):
  print("#", end='')
print("")
for _ in range(h):
  print("#", end='')
  print(input(), end='')
  print("#", end='')
  print("")
for _ in range(w+2):
  print("#", end='')