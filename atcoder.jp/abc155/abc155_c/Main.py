import collections
s = collections.Counter([input() for i in range(int(input()))])
cnt = max(s.values())
[print(i) for i in sorted(s.keys()) if s[i] == cnt]