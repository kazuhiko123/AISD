n = int(input())
used = set()
next_id = {}

for _ in range(n):
    name = input().strip()

    if name not in used:
        used.add(name)
        print("OK")

    else:
        i = next_id.get(name, 1)
        while (name +str(i)) in used:
            i += 1
        new_name = name + str(i)
        used.add(new_name)
        next_id[name] = i + 1
        print(new_name)

