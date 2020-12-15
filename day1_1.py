"""https://adventofcode.com/2019/day/1"""
with open('input1.txt') as f:
    INPUT = [line.rstrip() for line in f]

OUTPUT = 0


def get_fuel(mass):
    return int(mass / 3) - 2


for module in INPUT:
    OUTPUT += get_fuel(int(module))

print(OUTPUT)
