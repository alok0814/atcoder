n = int(input())
a = list(map(int, input().split()))
flag = False
cnt = 0
while flag == False:
  for i in range(n):
    if a[i] % 2 != 0:flag = True
    else:a[i]  = a[i] // 2
  cnt += 1
print(cnt-1)