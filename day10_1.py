IN = [x.split("\n")[0] for x in open("input10.txt", "r").readlines()]
IN = [[char for char in IN[i]] for i in range(len(IN))]


def isInSight(pos1, pos2):
    points = abs(pgcd(pos2[0] - pos1[0], pos2[1] - pos1[1])) - 1
    if (points == -1 or points == 0):
        return 1
    increX = (pos2[0] - pos1[0]) / (points + 1)
    increY = (pos2[1] - pos1[1]) / (points + 1)

    cx = pos1[0]
    cy = pos1[1]
    for i in range(points):
        cx += increX
        cy += increY
        if (IN[int(cy)][int(cx)] != "."):
            return 0
    return 1


def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def toString():
    s = ""
    for y in range(h):
        for x in range(w):
            s += str(IN[y][x]) + " "
        s += "\n"
    print(s)


h = len(IN)
w = len(IN[0])

toString()

for y in range(h):
    for x in range(w):
        if IN[y][x] != ".":
            sum = 0
            for j in range(h):
                for i in range(w):
                    if IN[j][i] != "." and (i != x or y != j):
                        sum += isInSight((x, y), (i, j))
            IN[y][x] = str(sum)

max = 0
for y in range(h):
    for x in range(w):
        if IN[y][x] != "." and int(IN[y][x]) > max:
            max = int(IN[y][x])

toString()

print(max)