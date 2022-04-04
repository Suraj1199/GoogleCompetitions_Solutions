from random import sample, choice, shuffle
from sys import stdin, stdout
finput = stdin.readline
fprint = stdout.write
def walk():
    fprint('W\n')
    stdout.flush()
    return map(int, finput().split())
def teleport(t):
    fprint('T ' + str(t) + '\n')
    stdout.flush()
    return map(int, finput().split())
for T in range(int(finput())):
    n, k = map(int, finput().split()) 
    v = set(range(1, n + 1))
    r, p = map(int, finput().split())
    e = p
    v.remove(r)
    w = 1
    for i in range(k):
        if not v:
            break
        if i % 2 == 0:
            pp = p
            r, p = walk()
            e += p * (pp / p)
            w += pp / p
        else:
            r, p = teleport(next(iter(v)))
            e += p
            w += 1
        if r in v:
            v.remove(r)    
    fprint('E ' + str(int(e / w * n / 2)) + '\n')    
    stdout.flush()
    