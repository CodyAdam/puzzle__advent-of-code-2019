"""https://adventofcode.com/2019/day/1"""

with open('input1.txt') as f:
    INPUT = [line.rstrip() for line in f]

OUTPUT = 0


def get_fuel(mass):
    fuel = int(mass / 3) - 2
    if fuel > 0:
        fuel += get_fuel(fuel)
    return max(fuel, 0)


for module in INPUT:
    OUTPUT += get_fuel(int(module))

print(OUTPUT)
