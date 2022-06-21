a,b,c,k=map(int,input().split())
ans = b-a if k%2 else a-b
print("Unfair") if abs(ans)>10**18 else print(ans)
