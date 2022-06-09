N = int(input())
if int(int(N // 1.08) * 1.08) == N : print(int(N // 1.08))
elif int(int(N // 1.08 + 1) * 1.08) == N : print(int(N // 1.08 + 1))
else:print(':(')
