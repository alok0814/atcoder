A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
bingo = False
#fuck object thinking
for _ in range(N):
    n = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == n:
                A[i][j] = 0

for i in range(3):
    sum = 0
    for j in range(3):
      sum += A[i][j]
    if sum == 0: bingo = True

if A[0][0]+A[1][1]+A[2][2] == 0 or A[0][2]+A[1][1]+A[2][0] == 0: bingo = True

for i in range(3):
  sum = 0
  for j in range(3):
    sum += A[j][i]
  if sum == 0: bingo = True

if bingo : print('Yes') 
else: print('No')