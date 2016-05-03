class HeapNode(object):
    def __init__(self, arg=None):
        super(HeapNode, self).__init__()
        self.val = arg

    val = None
    left = None
    right = None
    parent = None
    is_left = False
    is_right = False


class Heap(object):
    def __init__(self, arg=None):
        super(Heap, self).__init__()
        if arg is not None:
            for x in arg:
                self.add_element(x)

    def add_element(self, val=None):
        if self.root is None:
            node = HeapNode(val)
            self.root = node
            self.last_node = node
        else:
            if self.last_node is self.root:
                node = HeapNode(val)
                self.root.left = node
                self.last_node = node
                node.is_left = True
                node.parent = self.root
            else:
                if self.last_node.is_left:
                    node = HeapNode(val)
                    self.last_node.parent.right = node
                    node.parent = self.last_node.parent
                    self.last_node = node
                    node.is_right = True
                else:
                    parent_node = self.last_node.parent
                    while parent_node is not None:
                        if parent_node.is_left:
                            break
                        else:
                            parent_node = parent_node.parent

                    if parent_node is not None:
                        this_node = parent_node.parent.right
                        while this_node.left is not None:
                            this_node = this_node.left
                        node = HeapNode(val)
                        this_node.left = node
                        node.parent = this_node
                        node.is_left = True
                        self.last_node = node
                    else:
                        left_node = self.root.left
                        while left_node.left is not None:
                            left_node = left_node.left

                        node = HeapNode(val)
                        left_node.left = node
                        node.parent = left_node
                        node.is_left = True
                        self.last_node = node

    def pre_in_order(self, arrow):
        if arrow is self.root:
            del self.pre_string[:]
        if arrow is not None:
            self.pre_string.append(arrow.val)
            self.pre_in_order(arrow.left)
            self.pre_in_order(arrow.right)
            return self.pre_string

    def find_min(self):
        pass

    def remove_min(self):
        pass

    def reorder(self, arrow):
        if arrow.left.left is not None:
            self.reorder(arrow.left)


    root = None
    last_node = None
    pre_string = []


tree = Heap([28, 10, 30, 5, 9, 15, 12, 22, 18, 13, 27, 1])
print (tree.pre_in_order(tree.root))
