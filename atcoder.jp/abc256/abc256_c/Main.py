h1,h2,h3,w1,w2,w3 = map(int,input().split())
ans = 0
for A in range(1,31):
  for B in range(1,31):
    for D in range(1,31):
      for E in range(1,31):
        C = h1-A-B
        F = h2-D-E
        G = w1-A-D
        H = w2-B-E
        I = w3-C-F
        if C > 0 and F > 0 and G > 0 and H > 0 and I > 0 and I == h3-G-H:
          ans += 1
print(ans)