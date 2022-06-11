n = int(input())
d = list(map(int, input().split()))
d.sort()
half = len(d) // 2
ans = d[half] - d[half - 1]
print(ans)