N,M = map(int,input().split())
L = []
R = []

for _ in range(M):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)

st = max(L)
ed = min(R)

print(max(ed-st+1,0))