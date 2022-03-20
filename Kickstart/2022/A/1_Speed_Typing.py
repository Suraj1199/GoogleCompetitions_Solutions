def solve(s, p):
    ans = 0
    while s and p:
        if s[-1] == p[-1]:
            s.pop()
            p.pop()
            continue
        while p and s[-1] != p[-1]:
            ans += 1
            p.pop()
    if s:
        return 'IMPOSSIBLE'
    else:
        return ans + len(p)
    
for t in range(int(input())):
    s = list(input()[::-1])
    p = list(input()[::-1])
    print(f'Case #{t + 1}: {solve(s, p)}')
