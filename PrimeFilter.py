import math


def remove_num(ary, base):
    step = 2
    while base * step <= ary[-1]:
        if base * step in ary:
            pos = ary.index(base * step)
            ary.pop(pos)
        step += 1
    return ary


count = int(raw_input("Please input the count\n"))
ary = [x for x in range(2, count + 1)]
base = ary[0]
while math.pow(base, 2) < ary[-1]:
    ary = remove_num(ary, base)
    base = ary[ary.index(base)+1]
print ary