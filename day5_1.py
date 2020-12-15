"""https://adventofcode.com/2019/day/5"""

IN = open('input5.txt').readline().split(",")
IN = [int(x) for x in IN]
IN_PARAM = 1

OUT = IN.copy()


def operation(param3, param2, param1, oper, val1, val2, val3):
    """Send the operation result"""

    if oper == 1:
        OUT[val3] = (val1 if param1 == 1 else OUT[val1]) + (val2 if param2 == 1
                                                            else OUT[val2])
        return 4
    elif oper == 2:
        OUT[val3] = (val1 if param1 == 1 else OUT[val1]) * (val2 if param2 == 1
                                                            else OUT[val2])
        return 4
    elif oper == 3:
        OUT[val1] = IN_PARAM
        return 2
    elif oper == 4:
        print(val1 if param1 == 1 else OUT[val1])
        return 2
    elif oper == 99:
        return -1
    return -1


watch = 0
while watch < len(IN):
    print(watch)
    opcode = [int(char) for char in str(OUT[watch])]
    param3 = 0 if len(opcode) <= 4 else opcode[-5]
    param2 = 0 if len(opcode) <= 3 else opcode[-4]
    param1 = 0 if len(opcode) <= 2 else opcode[-3]
    oper = opcode[-1] if len(opcode) == 1 else int(
        str(opcode[-2]) + str(opcode[-1]))
    increment = operation(param3, param2, param1, oper, OUT[watch + 1],
                          OUT[watch + 2], OUT[watch + 3])
    if increment == -1:
        break
    watch += increment
