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


class DAG:
    def __init__(self, args):
        self._node_ary = []
        for x in args:
            if len(self._node_ary) == 0:
                self._node_ary = [Node(x, args.index(x))]
            else:
                self._node_ary.append(Node(x, args.index(x)))

        self._node_edge = Edge(len(args))
        self._stack = []

    def add_node_edge(self, start, end, val):
        self._node_edge.add_edge(start, end, val)

    def remove_node(self, row_num):
        self._node_edge.edge_marix.pop(row_num)
        for x in self._node_edge.edge_marix:
            x.pop(row_num)

    def topo_order(self):
        stack_len = len(self._stack)
        ary_len = len(self._node_ary)
        tmp_node_ary = self._node_ary
        while stack_len != ary_len:
            marix_len = ary_len - stack_len
            for x in range(0, marix_len):
                zero_count = 0
                for y in range(0, marix_len):
                    if self._node_edge.edge_marix[y][x] == 0:
                        zero_count += 1
                if zero_count == marix_len:
                    stack_len += 1
                    self._stack.append(tmp_node_ary[x])
                    self.remove_node(x)
                    tmp_node_ary.pop(x)
                    break

        for z in self._stack:
            print z.val


dag = DAG(['a', 'b', 'c', 'e', 'f'])
dag.add_node_edge(0, 1, 1)
dag.add_node_edge(0, 4, 1)
dag.add_node_edge(1, 2, 1)
dag.add_node_edge(3, 1, 1)
dag.add_node_edge(4, 2, 1)
dag.topo_order()
