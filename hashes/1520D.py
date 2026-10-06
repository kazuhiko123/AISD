import sys
from collections import defaultdict

def solve():
    input_data =  sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))

    for _ in range(t):
        n = int(next(iterator))
        cnt = defaultdict(int)

        for i in range(1, n+1):
            a_i = int(next(iterator))
            key = a_i - i
            cnt[key] += 1

        ans = 0
        for k in cnt.values():
            ans += k * (k - 1) // 2

        print(ans)

if __name__ == '__main__':
    solve()
