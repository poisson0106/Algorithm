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


    @property
    def edge_marix(self):
        return self._edge_marix

    @edge_marix.setter
    def edge_marix(self, times):
        self._edge_marix = [[0 for cols in range(0, times)] for rows in range(0, times)]

    def add_edge(self, start, end, val):
        print self._edge_marix[0][3]
        # self._edge_marix[start][end] = val
        # self._edge_marix[end][start] = val


class Prim:
    def __init__(self, args):
        for x in args:
            self._node_ary = Node(x)

        self._node_edge = Edge(len(args))

    @property
    def node_ary(self):
        return self._node_ary

    @node_ary.setter
    def node_ary(self, val):
        if self._node_ary is None:
            self._node_ary = [val]
        else:
            self._node_ary.append(val)

    @property
    def node_edge(self):
        return self._node_edge

    @node_edge.setter
    def node_edge(self, val):
        self._node_edge = val


a = Edge(5)
a.edge_marix = 5
a.add_edge(0, 3, 5)
print a
