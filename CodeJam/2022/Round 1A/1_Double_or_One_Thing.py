import collections
for T in range(int(input())):
    s = input() + '.'
    q = []
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            c += 1
        else:
            q.append((s[i], c))
            c = 0
    for i in range(len(q) - 1):
        pass
    print(f'Case #{T + 1}: {min(q)}')


