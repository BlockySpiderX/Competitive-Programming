t = int(input())

for i in range(t):
    n, h, l = map(int, input().split())
    
    if h > l:
        h, l = l, h

    x = 0
    y = 0

    for i in map(int, input().split()):
        if i <= h:
            x += 1
        if i <= l:
            y += 1

    print(min(x, y // 2))