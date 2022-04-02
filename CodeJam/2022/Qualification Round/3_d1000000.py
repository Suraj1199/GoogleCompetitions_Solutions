from collections import Counter
from sys import stdin, stdout
finput = stdin.readline
fprint = stdout.write
for T in range(int(finput())):
    n = int(finput())
    a = list(map(int, finput().split()))
    a.sort()
    l = 0
    for i in range(n):
        if l < a[i]:
            l += 1
    fprint(f'Case #{T + 1}: {l}\n')
        
         
    
