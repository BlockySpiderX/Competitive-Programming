n, m, a, b = map(int, input().split())

special = n // m
rem = n % m

costRem = min(rem * a, b)

ans = special * b + costRem
ans = min(ans, n * a)

print(ans)