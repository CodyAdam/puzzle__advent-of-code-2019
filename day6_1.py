LINES = open('input6.txt').read().split("\n")
LINES = [x.split(')') for x in LINES]
IN = set()
[IN.add((A, B)) for (A, B) in LINES]


def get_childs(p_name, depth):
    childs = []
    for (A, B) in IN:
        if A == p_name:
            child = {}
            child['name'] = B
            child['depth'] = depth + 1
            child['childs'] = get_childs(B, depth + 1)
            childs.append(child)
    return childs


def count_total_depth(parent):
    sum = 0
    for child in parent:
        sum += child['depth'] + count_total_depth(child['childs'])
    return sum


COM = [{'name': 'COM', 'depth': 0, 'childs': get_childs('COM', 0)}]

print(count_total_depth(COM))
