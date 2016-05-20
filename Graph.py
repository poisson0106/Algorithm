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

    # This part needs to be tested
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

    def remove_node(self):
        pass

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

    ary = []
    len = 0


ary = ['a', 'e', 'q', 'y', 'x']
graph = Graph(ary)
print (graph.has_edge('q', 'a'))
