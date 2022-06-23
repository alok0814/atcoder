n = int(input())
W = [input() for _ in range(n)]
print("Yes" if all(W[i][-1] == W[i+1][0] for i in range(n-1)) and len(W) == len(set(W)) else "No")



