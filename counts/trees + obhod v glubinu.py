import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))

    cats_in_v = [0] + [int(next(iterator)) for _ in range(n)]

    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        g[u].append(v)
        g[v].append(u)

    ans = 0
    stack = [(1, -1, 0)]

    while stack:
        v, parent, cat = stack.pop()

        if cats_in_v[v] == 1:
            cat += 1
        else:
            cat = 0

        if cat > m:
            continue

        is_leaf = True
        for neighbor in g[v]:
            if neighbor != parent:
                is_leaf = False
                stack.append((neighbor, v, cat))

        if is_leaf:
            ans += 1

    print(ans)


if __name__ == '__main__':
    solve()