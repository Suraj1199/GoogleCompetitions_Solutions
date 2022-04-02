for T in range(int(input())):
    a = [[float('inf'), i] for i in range(4)]
    for i in range(3):
        c = list(map(int, input().split()))
        for i in range(4):
            a[i][0] = min(a[i][0], c[i])
    a.sort(reverse=True)
    n = 1000000
    ans = [0] * 4
    for i in range(4):
        if n > 0:
            ans[a[i][1]] = min(n, a[i][0])
            n -= a[i][0]
    print(f'Case #{T + 1}:', end=" ")
    if n > 0:
        print('IMPOSSIBLE')
    else:
        print(' '.join(map(str, ans)))
    