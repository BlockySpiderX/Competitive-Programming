import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
vis = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(u):
    vis[u] = True
    for v in adj[u]:
        if not vis[v]:
            dfs(v)

reps = []

for i in range(1, n + 1):
    if not vis[i]:
        reps.append(i)
        dfs(i)

print(len(reps) - 1)

for i in range(1, len(reps)):
    print(reps[i - 1], reps[i])