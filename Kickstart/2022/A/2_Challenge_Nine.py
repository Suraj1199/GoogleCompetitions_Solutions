def solve(n):
    s = str(n)
    if n % 9 == 0:
        return s[0] + '0' + s[1:]
    r = str(9 - (n % 9))
    i = 0
    while i < len(s):
        if s[i] > r:
            break
        i += 1
    return s[:i] + r + s[i:]

for t in range(int(input())):
    n = int(input())
    print(f'Case #{t + 1}: {solve(n)}')
