import sys
from array import array


def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    max_nodes = 600005  # с запасом

    trans = array('i', [-1]) * (3 * max_nodes)
    is_end = bytearray(max_nodes)
    node_count = 1  # корень = узел 0

    def add_string(s):
        nonlocal node_count
        node = 0
        for char in s:
            c = ord(char) - ord('a')  # 0, 1, 2
            idx = node * 3 + c
            if trans[idx] == -1:
                trans[idx] = node_count
                node_count += 1
            node = trans[idx]
        is_end[node] = 1

    for _ in range(n):
        add_string(input().strip())

    def check(s):
        stack = [(0, 0, 0)]
        while stack:
            node, pos, changed = stack.pop()

            if pos == len(s):
                if changed == 1 and is_end[node]:
                    return True
                continue

            target = ord(s[pos]) - ord('a')

            nxt = trans[node * 3 + target]
            if nxt != -1:
                stack.append((nxt, pos + 1, changed))

            if changed == 0:
                for c in range(3):
                    if c == target:
                        continue
                    nxt = trans[node * 3 + c]
                    if nxt != -1:
                        stack.append((nxt, pos + 1, 1))

        return False

    for _ in range(m):
        s = input().strip()
        print("YES" if check(s) else "NO")


if __name__ == "__main__":
    solve()