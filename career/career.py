def solve(tri):
    while len(tri) > 1:
        t0 = tri.pop()
        print('t0=' + str(t0))
        t1 = tri.pop()
        print('t1=' + str(t1))
        tri.append([max(t0[i], t0[i + 1]) + t for i, t in enumerate(t1)])
        print('tri=' + str(tri))
    return tri[0][0]

data = open('input.txt', 'r').read()
# solve(data)

print(solve([map(int, row.split()) for row in data.splitlines()]))
