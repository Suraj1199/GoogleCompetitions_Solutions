import sys
finput = sys.stdin.readline
fprint = sys.stdout.write
sys.setrecursionlimit(10 ** 6)

def dfs(i):
    if not g[i]:
        return f[i]
    global ans
    s, m = 0, float('inf')
    for j in g[i]:
        x = dfs(j)
        s += x
        m = min(m, x)
    ans += (s - m)
    return max(m, f[i])

for T in range(int(finput())):
    n = int(finput())
    g = {i:[] for i in range(n + 1)}
    f = [0] + list(map(int, finput().split()))
    for u, v in enumerate(map(int, finput().split())):
        g[v].append(u + 1)
    ans = 0
    x = dfs(0)
    ans += x
    fprint(f'Case #{T+1}: {ans}\n')