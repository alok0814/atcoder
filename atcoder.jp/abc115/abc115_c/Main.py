n, k, *h = map(int, open(0).read().split())
h.sort()
print(min([h[i + k - 1] - h[i] for i in range(len(h) - k + 1)]))
