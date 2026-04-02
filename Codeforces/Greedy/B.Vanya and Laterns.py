n,l = map(int,input().split())
laterns = list(map(int,input().split()))

maxx = 0

laterns.sort()

#print(laterns)
for i in range(1,len(laterns)):
    maxx = max(maxx,laterns[i] - laterns[i-1])


ans = max(laterns[0], l- laterns[-1], maxx /2)

print(f"{ans:.10f}")