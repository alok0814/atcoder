from itertools import accumulate
import itertools
import sys
sys.setrecursionlimit(10**9)
import math
import heapq
import bisect
from collections import deque, Counter, defaultdict, OrderedDict
from sys import stdin
import copy
from decimal import Decimal
from operator import mul
from functools import reduce


MOD = 10 ** 9 + 7
def int1(x): return int(x) - 1
def stinput(): return stdin.readline()[:-1]
def ii(): return int(stinput())  # int input
def mi(): return map(int, stdin.readline().split())  # map input (int)
def li(): return list(mi())  # lis input (int)
def mi1(): return map(int1, stdin.readline().split())  # map input (int)-1
def li1(): return list(mi1())  # lis input (int)-1
def mis(): return map(str, stdin.readline().split())  # map input (string)
def lis(): return list(mis())  # lis input (string)
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

ans = 0
cnt = ''
ans1 = 0
tmp = ''
se = set()
se1 = set()
S = input()
S_reverse = S[::-1]
for moji in S:
    tmp = tmp + moji
    if tmp != cnt:
        cnt = tmp
        tmp = ''
        ans += 1

print(ans)
