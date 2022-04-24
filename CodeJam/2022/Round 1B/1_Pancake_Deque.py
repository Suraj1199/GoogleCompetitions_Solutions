from collections import deque
from sys import stdin, stdout
fprint = stdout.write
finput = stdin.readline
for T in range(int(finput())):
    n = int(finput())
    dq = deque(map(int, finput().split()))
    ans = p = 0
    for _ in range(n):
        if dq[0] < dq[-1]:
            ans += (dq[0] >= p)
            p = max(p, dq.popleft())
        else:
            ans += (dq[-1] >= p)
            p = max(p, dq.pop())
    fprint(f'Case #{T + 1}: {ans}\n')