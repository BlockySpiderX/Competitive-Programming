t = int(input())

for i in range(t):
    n = int(input())

    ans = []

    for i in range(1,n+1):
        if n != 1:
            ans.append(i)
            

    if n == 1:
        print(1)
    else:
        print(*ans)