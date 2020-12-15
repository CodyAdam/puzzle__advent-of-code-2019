"""https://adventofcode.com/2019/day/6"""
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


def contain(parent, name):
    if parent['name'] == name:
        return True
    for child in parent['childs']:
        if child['name'] == name or (True in [
                contain(c, name) for c in child['childs']
        ]):
            return True
    return False


def get_common_parent(parent, name1, name2):
    common = False
    for child in parent['childs']:
        if contain(child, name1) and contain(child, name2):
            common = get_common_parent(child, name1,
                                       name2) if get_common_parent(
                                           child, name1, name2) else child
    return common


# def get_in(name, parent):
#     if parent['name'] == name:
#         return parent
#     result = False
#     for child in parent['childs']:
#         if get_in(name, child) is not False:
#             result = get_in(name, child)
#     return result
def get_in(name, parent):
    if parent['name'] == name:
        return parent
    if contain(parent, name):
        arr = [get_in(name, child) for child in parent['childs']]
        return [x for x in arr if x != False][0]
    else:
        return False


COM = {'name': 'COM', 'depth': 0, 'childs': get_childs('COM', 0)}

YOU = get_in('YOU', COM)

SAN = get_in('SAN', COM)

COMMON = get_common_parent(COM, 'YOU', 'SAN')

DIST_YOU_SAN = SAN['depth'] + YOU['depth'] - 2 * COMMON['depth'] - 2

print(DIST_YOU_SAN)