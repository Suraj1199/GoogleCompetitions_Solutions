from sys import stdin, stdout
from collections import deque
fprint = stdout.write
finput = stdin.readline

def is_palin(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def solve(s, n):
    if n < 5:
        return 'POSSIBLE'
    states = deque([''])
    for i in range(5):
         for _ in range(len(states)):
            state = states.popleft()
            if s[i] == '?':
                    states.append(state + '0')
                    states.append(state + '1')
            else:
                states.append(state + s[i])
    for i in range(5, n):
        size = len(states)
        for _ in range(size):
            state = states.popleft()
            if s[i] != '?':
                new_states = [state[1:] + s[i]]
            else:
                new_states = [state[1:] + '0', state[1:] + '1']
            for new_state in new_states:
                if not (is_palin(state) or is_palin(new_state) or is_palin(state + new_state[-1])):
                    states.append(new_state)
        if len(states) == 0:
            return 'IMPOSSIBLE'
    return 'POSSIBLE'
                    

for t in range(int(finput())):
    n = int(finput().strip())
    s = finput().strip()
    fprint(f'Case #{t + 1}: {solve(s, n)}\n')
