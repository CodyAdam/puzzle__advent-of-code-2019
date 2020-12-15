import math

IN = [x for x in open("input14.txt", "r").read().splitlines()]

for i in range(len(IN)):
    IN[i] = IN[i].split(" => ")
    IN[i][0] = [x.split(" ") for x in IN[i][0].split(", ")]
    IN[i][1] = IN[i][1].split(" ")
    print(IN[i])


def find(str):
    for reaction in IN:
        if (reaction[1][1] == str):
            return reaction


def need(str, num):
    if (str == "ORE"):
        return float(num)
    react = find(str)
    ore = 0
    for chemical in react[0]:
        ore += need(chemical[1], chemical[0]) / int(react[1][0])
    return math.(float(ore) * float(num))


print(need("A", 1))
print(need("B", 1))
print(need("C", 1))
print(need("D", 1))
print(need("E", 1))
print(need("FUEL", 1))