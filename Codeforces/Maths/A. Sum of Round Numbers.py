t = int(input())


def split(n):
    ans = []
    place = 1

    while n> 0:
        digit = n%10

        if digit != 0:
            ans.append(digit* place)

        n//= 10
        place*=10

    return ans[::-1]


for i in range(t):
    n = int(input())

    n = str(n)

    zero = 0

    for i in n:
        if i == "0":
            zero += 1

    x = len(n) - zero


    if x == 1:
        print(1)
        print(int(n))
    else:
        print(len(n) -zero)
        print(*split(int(n)))