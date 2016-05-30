class Node:
    def __init__(self, *args):
        self._val = args[0]
        self._is_visit = False

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, arg):
        self._val = arg

    @property
    def is_visit(self):
        return self._is_visit

    @is_visit.setter
    def is_visit(self, arg):
        self._is_visit = arg


class Edge:
    def __init__(self, *args):
        self._edge_marix = [[0 for cols in range(0, args[0])] for rows in range(0, args[0])]

    @property
    def edge_marix(self):
        return self._edge_marix

    def add_edge(self, start, end, val):
        self._edge_marix[start][end] = val
        self._edge_marix[end][start] = val


class Prim:
    def __init__(self, args):
        self._node_ary = []
        for x in args:
            if len(self._node_ary) == 0:
                self._node_ary = [x]
            else:
                self._node_ary.append(x)

        self._node_edge = Edge(len(args))

    @property
    def node_ary(self):
        return self._node_ary

    @node_ary.setter
    def node_ary(self, val):
        self._node_ary.append(val)

    @property
    def node_edge(self):
        return self._node_edge

    def add_node_edge(self, start, end, val):
        self._node_edge.add_edge(start, end, val)

    @property
    def stack(self):
        return self._stack

    @stack.setter
    def stack(self, ele):
        if self._stack is None:
            self._stack = [ele]
        else:
            self._stack.append(ele)

    def cal(self):
        if self._stack is None:
            self._stack = [self._node_ary[0]]
        else:
            while len(self._stack) != len(self._node_ary):
                pass


ary = ['a', 'b', 'c', 'd', 'e', 'f']
table = Prim(ary)
table.add_node_edge(0, 1, 6)
table.add_node_edge(0, 2, 1)
table.add_node_edge(0, 3, 5)
table.add_node_edge(1, 2, 5)
table.add_node_edge(1, 4, 5)
table.add_node_edge(2, 3, 5)
table.add_node_edge(2, 4, 6)
table.add_node_edge(2, 5, 4)
table.add_node_edge(3, 5, 2)
table.add_node_edge(4, 5, 6)
print table.node_ary
