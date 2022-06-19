a,b = map(int, input().split())
if a * b <= 0:
  print("Zero")
elif (b-a)%2 == 0 and a < 0:
  print("Negative")
else:
  print("Positive")