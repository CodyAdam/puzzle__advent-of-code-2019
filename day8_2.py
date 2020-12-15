IN = [char for char in open("input8.txt", "r").read()]

h = 6
w = 25

#number of layers
n = int(len(IN) / (h * w))


def toString(l):
    s = ""
    for y in range(h):
        for x in range(w):
            s += str(l[y][x])
        s += "\n"
    print(s)


def count(find, layer):
    sum = 0
    for y in range(h):
        for x in range(w):
            if (str(layer[y][x]) == str(find)):
                sum += 1
    return sum


layer = [[["#" for x in range(w)] for y in range(w)] for i in range(n)]

for i in range(n):
    for y in range(h):
        for x in range(w):
            layer[i][y][x] = IN[(w * h * i) + (w * y) + x]

flat = [["2" for x in range(w)] for y in range(w)]

for i in range(n):
    for y in range(h):
        for x in range(w):
            if (flat[y][x] == str(2)):
                flat[y][x] = layer[i][y][x]

toString(flat)
