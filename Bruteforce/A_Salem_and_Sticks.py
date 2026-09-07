n = int(input())
a = list(map(int, input().split()))

ans = float('inf')
t = 1

for i in range(1, 101):
    res = 0

    for j in range(n):
        res += min(
            min(abs(a[j] - i - 1), abs(a[j] - i + 1)),
            
            abs(a[j] - i)
        )

    if res < ans:
        ans = res
        t = i

print(t, ans)