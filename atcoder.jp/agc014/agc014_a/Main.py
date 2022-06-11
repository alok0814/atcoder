A,B,C = map(int, input().split())
n = 0
if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:print(0) 
elif A == B == C:print(-1)
else:
  while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    give_a = A // 2
    A /= 2
    give_b = B // 2
    B /= 2
    give_c = C // 2
    C /= 2
    A = give_b + give_c
    B = give_a + give_c
    C = give_a + give_b
    n += 1
  print(n)
