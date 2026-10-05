import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        g[u].append((v, w))
        g[v].append((u, w))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    parent = [0] * (n + 1)
    pq = [(0, 1)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == n:
            break
        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[n] == float('inf'):
        print(-1)
    else:
        path = []
        curr = n
        while curr != 0:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        print(*path)


if __name__ == '__main__':
    solve()