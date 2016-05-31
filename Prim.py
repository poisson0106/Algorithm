class Node:
    def __init__(self, *args):
        self._val = args[0]
        self._position = args[1]

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, arg):
        self._val = arg

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val):
        self._position = val


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
                self._node_ary = [Node(x, args.index(x))]
            else:
                self._node_ary.append(Node(x, args.index(x)))

        self._node_edge = Edge(len(args))
        self._stack = None
        self._visited = []

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, val):
        self.visited.append(val)

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
        while self._stack is None or len(self._stack) != len(self._node_ary):
            if self._stack is None:
                self._stack = [self._node_ary[0]]
            else:
                scope_min = 999
                scope_min_pos_y = -1
                scope_min_pos_x = -1
                for x in self._stack:
                    for y in self._node_edge.edge_marix[x.position]:
                        tmp_x_pos = x.position
                        tmp_y_pos = self._node_edge.edge_marix[x.position].index(y)
                        if y != 0 and y < scope_min and [tmp_x_pos, tmp_y_pos] not in self._visited \
                                and [tmp_y_pos, tmp_x_pos] not in self._visited \
                                and self._node_ary[tmp_y_pos] not in self._stack:
                            scope_min = y
                            scope_min_pos_y = tmp_y_pos
                            scope_min_pos_x = tmp_x_pos

                self._stack.append(self._node_ary[scope_min_pos_y])
                self._visited.append([scope_min_pos_x, scope_min_pos_y])
                self._visited.append([scope_min_pos_y, scope_min_pos_x])

        for z in self._stack:
            print z.val + ","


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
table.cal()
