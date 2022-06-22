n = int(input())
a = [int(input()) for _ in range(n)]
cnt = 1
s = a[0]
while s != 2 and cnt < n:
  cnt += 1
  s = a[s-1]
print(cnt if cnt < n else -1)