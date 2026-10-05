import sys
sys.setrecursionlimit(5000)

def solve():
    max_depth = 0
    n = int(input())
    dependence = []
    roots = []

    for _ in range(n+1):
        dependence.append([])

    for i in range(1, n+1):
        p= int(input())

        if p == -1:
            roots.append(i)
        else:
            dependence[p].append(i)

    def dfs(w, depth):
        nonlocal max_depth
        if depth > max_depth:
            max_depth = depth

        for worker in dependence[w]:
            dfs(worker, depth + 1)
    for root in roots:
        dfs(root, 1)

    print(max_depth)

if __name__ == "__main__":
    solve()