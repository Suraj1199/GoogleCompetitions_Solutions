# ONLY PASSES TEST CASE 1

from sys import stdin, stdout
fprint = stdout.write
finput = stdin.readline

MAX = int(1e5 + 1)
dp = [0] * MAX
def check(n):
    p, s = 1, 0
    for i in map(int, str(n)):
        p *= i
        s += i
    return p % s == 0

for i in range(1, MAX):
    dp[i] = dp[i - 1] + check(i)

def solve(a, b):
    return dp[b] - dp[a - 1]
   
for t in range(int(input())):
    a, b = map(int, finput().strip().split())
    fprint(f'Case #{t + 1}: {solve(a, b)}\n')

