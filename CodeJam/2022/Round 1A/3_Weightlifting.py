# from functools import lru_cache
# @lru_cache

def solve(a, e, w, st, i=0, k=0):
    if i >= e:
        return
    for j in range(w):
        if a[i][j] != st[i][j]:
            st[i][j]
            solve(a, e, w, i, k + 1, st[j])
    if i == e - 1:
        ans = min(ans, k)
    solve(a, e, w, i + 1, k)
    

for T in range(int(input())):
    e, w = map(int, input().split())
    a = []
    for _ in range(e):
        a.append(list(map(int, input().split())))
    ans = float('inf')
    solve(a, e, w)
    print(f'Case #{T + 1}: {ans}')


