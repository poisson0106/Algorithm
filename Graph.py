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
        for x in range(0, self.len):
            for y in range(x + 1, self.len):
                is_linked = raw_input("Is " + self.ary[y].val + " linked to " + self.ary[x].val + "? 1 or 0\n")
                if is_linked == "1":
                    self.add_edge(x, y, self.ary[y].val)
                    self.add_edge(y, x, self.ary[x].val)

    def add_edge(self, start, end, val):
        if self.ary[start].head is None:
            self.ary[start].head = Edge(start, end, val)
        else:
            tmp = self.ary[start].head
            while tmp.next_edge is not None:
                tmp = tmp.next_edge
            tmp.next_edge = Edge(start, end, val)

    def add_node(self, val):
        self.ary.append(Node(val, self.len))
        self.len += 1

    def remove_edge(self):
        pass

    def remove_node(self):
        pass

    ary = []
    len = 0


ary = ['a', 'e', 'q', 'y', 'x']
graph = Graph(ary)
