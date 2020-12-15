"""https://adventofcode.com/2019/day/3"""
A, B = open("input3.txt").read().split('\n')
A, B = [x.split(",") for x in [A, B]]

OUTPUT = 0

DX = {"L": -1, "R": 1, "U": 0, "D": 0}
DY = {"L": 0, "R": 0, "U": 1, "D": -1}


def get_points(A):
    """dwa"""
    x = 0
    y = 0
    ans = set()
    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            ans.add((x, y))
    return ans


PA = get_points(A)
PB = get_points(B)

both = PA & PB
ans = min([abs(x) + abs(y) for (x, y) in both])
print(ans)
