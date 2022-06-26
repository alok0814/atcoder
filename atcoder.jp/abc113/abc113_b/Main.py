n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
d = [abs((t-x*0.006) - a) for x in h]
print(d.index(min(d))+1)
