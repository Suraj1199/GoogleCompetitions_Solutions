vowels = set(list('AEIOUaeiou'))
consonants = set(list('bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'))
for t in range(int(input())):
    s = input()
    print(f"Case #{t + 1}: {s} is ruled by ", end='')
    if s[-1] in vowels:
        print('Alice.')
    elif s[-1] in consonants:
        print('Bob.')
    else:
        print('nobody.')