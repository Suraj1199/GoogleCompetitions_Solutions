for T in range(int(input())):
    r, c = map(int ,input().split())
    n, m = 2 * r + 1, 2 * c + 1
    a = [['.'] * m for _ in range(n)]
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                if j % 2 == 0:
                    a[i][j] = '+'
                else:
                    a[i][j] = '-'
        else:
            for j in range(m):
                if j % 2 == 0:
                    a[i][j] = '|'
    for i in range(2):
        for j in range(2):
            a[i][j] = '.'
    print(f'Case #{T + 1}:')
    print('\n'.join(''.join(i) for i in a))
