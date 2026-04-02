n = int(input())

result = []



for i,digit in enumerate(str(n)):
    d = int(digit)

    if d == 9 and i == 0:
        result.append(str(d))
    elif d >= 5:
        result.append(str(int(9-d)))
    else:
        result.append(str(d))

print(''.join(result))