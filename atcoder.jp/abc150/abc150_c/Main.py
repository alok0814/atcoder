import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
lst = list(itertools.permutations(range(1, n+1)))
print(abs(lst.index(p) - lst.index(q)))