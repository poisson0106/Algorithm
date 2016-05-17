class Node:
    def __init__(self, val,pos):
        self.val = val
        self.position = pos

    val = ""
    position = 0
    head = None


class Edge:
    def __init__(self, *args):
        self.start = args[0]
        self.end = args[1]

    start = -1
    end = -1
    val = 1
    next_edge = None


class Graph:
    def __init__(self, ary):
        self.len = len(ary)
        tail = None
        for x in range(0,len(ary)):
            self.ary.append(Node(ary[x],x))
        for x in range(0, len):
            for y in range(x, len):
                is
    ary = []
    len = 0
