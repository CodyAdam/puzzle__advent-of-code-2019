"""https://adventofcode.com/2019/day/2"""

with open('input2.txt') as f:
    INPUT = f.readline()
INPUT = INPUT.split(",")
for i, _ in enumerate(INPUT):
    INPUT[i] = int(INPUT[i])


def operation(oper, target1, target2):
    """Send the operation result"""
    if oper == 1:
        return target1 + target2
    elif oper == 2:
        return target1 * target2
    else:
        raise Exception("Operation " + oper + " has been found !")


for NOUN in range(0, 100):
    for VERB in range(0, 100):

        INPUT[1] = NOUN
        INPUT[2] = VERB

        OUTPUT = INPUT.copy()

        WATCHING = 0

        while WATCHING < len(INPUT) - 1:
            if OUTPUT[WATCHING] == 99:
                break
            OUTPUT[OUTPUT[WATCHING + 3]] = operation(
                OUTPUT[WATCHING], OUTPUT[OUTPUT[WATCHING + 1]],
                OUTPUT[OUTPUT[WATCHING + 2]])
            WATCHING += 4

        if OUTPUT[0] == 19690720:
            print(100 * NOUN + VERB)
