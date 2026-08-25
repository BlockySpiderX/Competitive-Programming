t = int(input())

for i in range(t):
    n,s,x = map(int,input().split())
    nums = list(map(int,input().split()))

    y = s-sum(nums)
    

    if sum(nums) == s:
        print("YES")
    elif sum(nums) > s:
        print("NO")
    else:
        if y%x == 0:
            print("YES")
        else:
            print('NO') 