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

    def remove_edge(self, ele1, ele2):
        s_pos = -1
        e_pos = -1
        if self.has_edge(ele1, ele2):
            s_pos = self.find_pos(ele1)
            e_pos = self.find_pos(ele2)
            self.remove_from_table(s_pos, e_pos)
            self.remove_from_table(e_pos, s_pos)

    def remove_from_table(self, s_pos, e_pos):
        arrow = self.ary[s_pos].head
        while arrow is not None:
            if arrow.end == e_pos:
                if arrow.next_edge is None:
                    arrow = None
                    break
                else:
                    arrow.end = arrow.next_edge.end
                    arrow.val = arrow.next_edge.val
                    arrow.next_edge = arrow.next_edge.next_edge
                    break
            else:
                arrow = arrow.next_edge
                
    # Need to fix, since with the node removed, the position shoud be changed
    def remove_node(self, ele):
        pos = self.find_pos(ele)
        node = self.ary[pos]
        tmp = node.head
        while tmp is not None:
            self.remove_edge(node.val, self.ary[tmp.end].val)
            tmp = tmp.next_edge
        self.ary.pop(node.position)

    def has_edge(self, start, end):
        s_pos = self.find_pos(start)
        e_pos = self.find_pos(end)
        if s_pos == -1 or e_pos == -1:
            return False
        else:
            first = self.ary[s_pos].head
            result = False
            if first is not None:
                while first is not None:
                    if first.val == self.ary[e_pos].val:
                        result = True
                        break
                    else:
                        first = first.next_edge

            return result

    def find_pos(self, ele):
        pos = -1
        for x in self.ary:
            if x.val == ele:
                pos = x.position
        return pos

    def traverse_node_bf(self, node):
        if node.position in self.is_visited:
            return 0
        else:
            if node.head is not None:
                tmp = node.head
                while tmp is not None:
                    if tmp.end not in self.is_visited:
                        self.queue.append(self.ary[tmp.end])
                    tmp = tmp.next_edge
                self.queue.pop(0)
                self.is_visited.append(node.position)
                print (node.val)
                if len(self.queue) != 0:
                    self.traverse_node_bf(self.queue[0])
                else:
                    return 0
            else:
                self.is_visited.append(node.position)

    def traverse_node_df(self, node):
        if node.position not in self.is_visited:
            print(node.val)
            self.is_visited.append(node.position)
            tmp = node.head
            while tmp is not None:
                self.traverse_node_df(self.ary[tmp.end])
                tmp = tmp.next_edge
        else:
            return 0

    def bf_traverse(self):
        self.is_visited = []
        if len(self.ary) != 0:
            for x in range(0, len(self.ary)):
                if x not in self.is_visited:
                    self.traverse_node_bf(self.ary[x])
        else:
            print ("Error")

    def df_traverse(self):
        self.is_visited = []
        if len(self.ary) != 0:
            for x in range(0, len(self.ary)):
                if x not in self.is_visited:
                    self.queue.append(self.ary[x])
                    self.traverse_node_df(self.ary[x])
        else:
            print ("Error")

    ary = []
    len = 0
    queue = []
    is_visited = []


ary = ['a', 'e', 'q', 'y', 'x']
graph = Graph(ary)
graph.remove_edge('q', 'a')
graph.remove_node('q')
graph.bf_traverse()
# ary2 = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8']
# graph2 = Graph(ary2)
# graph2.remove_edge('v2', 'v5')
# graph2.df_traverse()
