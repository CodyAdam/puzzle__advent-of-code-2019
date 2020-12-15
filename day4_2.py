R = [int(x) for x in open('input4.txt').read().split('-')]


def is_accepted(n):
    arr = [int(char) for char in str(n)]

    rule3 = False
    for i in range(len(arr) - 1):
        if i == 0:
            if arr[i] == arr[i + 1] and arr[i + 1] != arr[i + 2]:
                rule3 = True
        elif i == 4:
            if arr[i] == arr[i + 1] and arr[i - 1] != arr[i]:
                rule3 = True
        else:
            if arr[i] == arr[i + 1] and arr[i - 1] != arr[i] and arr[
                    i + 1] != arr[i + 2]:
                rule3 = True

    rule4 = True
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            rule4 = False

    return rule3 and rule4


ans = 0
for n in range(R[1] - R[0]):
    if is_accepted(R[0] + n): ans += 1
print(ans)
