H, W = map(int, input().split())
grids = H * W
if H == 1 or W == 1 : print(1)
elif grids % 2 == 0 : print(int(grids / 2))
else : print(int(grids / 2 + 1))