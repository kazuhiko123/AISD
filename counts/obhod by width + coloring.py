from collections import deque
import sys
sys.setrecursionlimit(100000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    t = int(next(iterator))

    for _ in range(t):
        n = int(next(iterator))
        m = int(next(iterator))

        g =[[] for _ in range(n+1)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))

            g[u].append(v)
            g[v].append(u)

        visited = [0] * (n+1)
        color1 = []
        color2 = []

        queue = deque([(1, 1)])
        visited[1] = 1

        while queue:
            v, c = queue.popleft()
            if c == 1:
                color1.append(v)
            else:
                color2.append(v)

            for neighbor in g[v]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 3 - c
                    queue.append((neighbor, 3 - c))

        # Выбор меньшего списка
        if len(color1) <= len(color2):
            ans = color1
        else:
            ans = color2

        print(len(ans))
        print(*ans)

if __name__ == '__main__':
    solve()
