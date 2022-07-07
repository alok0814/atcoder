n, m = map(int,input().split())
wa = [0]*(n+1)
wa_cnt = 0
ac = set()

for i in range(m):
    p, s = map(str,input().split())
    if p in ac:
        continue
    if s == "WA":
        wa[int(p)] += 1
    else:
        ac.add(p)
        wa_cnt += wa[int(p)]

print(len(ac), wa_cnt)