N = int(input())
K = int(input())
x = list(map(int,input().split()))
sum = 0
for i in x:
  sum += min(i, K-i)*2
print(sum)