t = int(input())

for i in range(t):
    n = int(input())

    ans = []
    i = 1

    while len(ans) < n:
        if i % 3 != 0:
            ans.append(i)
        i += 1

    print(*ans)