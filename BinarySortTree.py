class ObjectItem(object):
    def __init__(self, arg=None):
        super(ObjectItem, self).__init__()
        self.val = arg

    val = None
    left = None
    right = None
    parent = None


class BinarySortTree(object):
    def __init__(self, ary):
        super(BinarySortTree, self).__init__()
        self.ary = ary
        if len(ary) > 0:
            for x in ary:
                if self.root is None:
                    self.add_element(val=x)
                else:
                    self.add_element(self.root, x)

    def add_element(self, pnode=None, val=None):
        if self.root is None:
            node = ObjectItem(val)
            self.root = node
            return 0
        else:
            if val > pnode.val:
                if pnode.right is None:
                    node = ObjectItem(val)
                    pnode.right = node
                    node.parent = pnode
                    return 0
                else:
                    self.add_element(pnode.right, val)
            else:
                if pnode.left is None:
                    node = ObjectItem(val)
                    pnode.left = node
                    node.parent = pnode
                    return 0
                else:
                    self.add_element(pnode.left, val)

    def remove_element(self, val):
        node = self.find(self.root, val)
        left_tree = node.left
        right_tree = node.right
        if left_tree is None and right_tree is None:
            node = None
        else:
            if left_tree is None:
                if node is self.root:
                    self.root = node.right
                else:
                    node.right.parent = node.parent
                    node.parent.right = node.right
                    node = None
            elif right_tree is None:
                if node is self.root:
                    self.root = node.left
                else:
                    node.left.parent = node.parent
                    node.parent.left = node.left
                    node = None
            else:
                tmp_arrow = left_tree.right
                if tmp_arrow is not None:
                    while tmp_arrow.right is not None:
                        tmp_arrow = tmp_arrow.right
                        node.val = tmp_arrow.val
                        if tmp_arrow.left is None:
                            tmp_arrow.parent.right = None
                            tmp_arrow = None
                        else:
                            tmp_arrow.val = tmp_arrow.left.val
                            tmp_arrow.left = None
                else:
                    left_tree.parent.val = left_tree.val
                    left_tree.parent.left = left_tree.left
                    left_tree.left.parent = left_tree.parent
                    left_tree = None


    def find_min(self):
        pass

    def find_max(self):
        pass

    def remove_min(self):
        pass

    def remove_max(self):
        pass

    def pre_in_order(self, arrow):
        if arrow is self.root:
            del self.pre_string[:]
        if arrow is not None:
            self.pre_string.append(arrow.val)
            self.pre_in_order(arrow.left)
            self.pre_in_order(arrow.right)
            return self.pre_string

    def find(self, arrow, val):
        if arrow is not None:
            if arrow.val == val:
                return arrow
            else:
                l = self.find(arrow.left, val)
                if l is not None:
                    return l
                r = self.find(arrow.right, val)
                if r is not None:
                    return r
                return None

    root = None
    pre_string = []
    ary = []


sort = BinarySortTree([8, 10, 20, 6, 4, 7, 15, 21, 3, 2])
print (sort.pre_in_order(sort.root))
sort.remove_element(6)
print (sort.pre_in_order(sort.root))
