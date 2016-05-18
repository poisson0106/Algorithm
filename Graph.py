class Node:
    def __init__(self, val, pos):
        self.val = val
        self.position = pos

    val = ""
    position = 0
    head = None


class Edge:
    def __init__(self, *args):
        self.start = args[0]
        self.end = args[1]
        self.val = args[2]

    start = -1
    end = -1
    val = 1
    next_edge = None


class Graph:
    def __init__(self, ary):
        self.len = len(ary)
        tail = None
        for x in range(0, len(ary)):
            self.ary.append(Node(ary[x], x))
        for x in range(0, len):
            for y in range(x, len):
                is_linked = raw_input("Is " + ary[y].val + " linked to" + ary[x].val + "? 1 or 0")
                if is_linked == "1":
                    if ary[x].head is None:
                        ary[x].head = Edge(x, y, ary[y].val)
                    else:
                        tmp = ary[x].head
                        while tmp.next_edge is not None:
                            tmp = tmp.next_edge
                        tmp.next_edge = Edge(x, y, ary[y].val)

    def add_edge(self,start,end val):
        

    ary = []
    len = 0
