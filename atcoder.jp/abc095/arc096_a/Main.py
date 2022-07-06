a, b, c, A, B = map(int, input().split())
x = a if A >= B else b
print(min(a*A + b*B, c * 2 * max(A, B), c * 2 * min(A, B) + x * abs(A-B)))