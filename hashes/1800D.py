import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)
t = int(next(iterator))

for _ in range(t):
    n = int(next(iterator))
    s =next(iterator)

    ans = n - 1

    for i in range(n-2):
        if s[i] == s[i + 2]:
            ans -= 1

    print(ans)