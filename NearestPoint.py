import math


def cal_distance(p_ary):
    dis = {}

    if len(p_ary == 2):
        tmp_dis = abs(p_ary[1][0] - p_ary[0][0]) + abs(p_ary[1][1] - p_ary[0][1])
        dis["point1"] = p_ary[0]
        dis["point2"] = p_ary[1]
        dis["dis"] = tmp_dis
    else:
        p1p2 = abs(p_ary[1][0] - p_ary[0][0]) + abs(p_ary[1][1] - p_ary[0][1])
        p1p3 = abs(p_ary[2][0] - p_ary[0][0]) + abs(p_ary[2][1] - p_ary[0][1])
        p2p3 = abs(p_ary[2][0] - p_ary[1][0]) + abs(p_ary[2][1] - p_ary[1][1])
        if p1p2 >= p1p3:
            if p1p3 >= p2p3:
                dis["point1"] = p_ary[1]
                dis["point2"] = p_ary[2]
                dis["dis"] = p2p3
            else:
                dis["point1"] = p_ary[0]
                dis["point2"] = p_ary[2]
                dis["dis"] = p1p3
        else:
            if p2p3 <= p1p2:
                dis["point1"] = p_ary[1]
                dis["point2"] = p_ary[2]
                dis["dis"] = p2p3
            else:
                dis["point1"] = p_ary[0]
                dis["point2"] = p_ary[1]
                dis["dis"] = p1p2

    return dis


def point_near_sort(p_ary):
    length = len(p_ary)
    dis = {}
    if length == 2 or length == 3:
        return cal_distance(p_ary)
    else:
        l_part_d = point_near_sort(p_ary[:length / 2])
        r_part_d = point_near_sort(p_ary[length / 2:])
        if l_part_d.get(dis)>=r_part_d.get(dis):
            dis = r_part_d
        else:
            dis = l_part_d

        d1dn = 




dis = 65536
Points = [(1, 2), (3, 5), (6, 1), (4, 7), (8, 3)]
Points.sort()
