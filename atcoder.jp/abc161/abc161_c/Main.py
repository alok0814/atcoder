n, k = map(int, input().split())
print(min(n%k, k - n%k))
# pre = N + K
# while pre > N:
#   pre = N
#   N = abs(N - K)
# print(pre)