t = int(input())


for i in range(t):
    x,y = map(int,input().split())

    if x< y or x%y != 0:
        print("NO")
    else:
        print("YES")