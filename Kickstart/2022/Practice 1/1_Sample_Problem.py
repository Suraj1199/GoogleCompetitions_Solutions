for t in range(int(input())):
    n, m = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    ans = sum(a) % m
    print(f"Case #{t+1}: {ans}")