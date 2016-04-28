class ObjectItem(object):
    def __init__(self, arg=None):
        super(ObjectItem, self).__init__()
        self.val = arg

    val = None
    left = None
    right = None
    parent = None


class BinarySortTree():
    def __init__(self):
        super(BinarySortTree, self).__init__()

    def add_element(self, pnode=None):
        if self.root is None:
            value = raw_input("Please input the value")
            node = ObjectItem(value)
            self.root = node
            isFinished = raw_input("If it is finished? Y or N?")
            if isFinished == "Y":
                return 0
            else:
                self.add_element(self.root)
        else:
            value = raw_input("Please input the value")
            node = ObjectItem(value)
            if value > pnode.val:
                if pnode.right is None:
                    pnode.right = node
                    node.parent = pnode
                    return 0
                else:
                    self.add_element(pnode.right)
            else:
                if pnode.left is None:
                    pnode.left = node
                    node.parent = pnode
                    return 0
                else:
                    self.add_element(pnode.left)

    def remove_element(self):
        pass

    def find_min(self):
        pass

    def find_max(self):
        pass

    def remove_min(self):
        pass

    def remove_max(self):
        pass

    def pre_in_order(self, arrow):
        if arrow is not None:
            self.pre_string.append(arrow.val)
            self.pre_in_order(arrow.left)
            self.pre_in_order(arrow.right)
            return self.pre_string

    root = None
    pre_string = []
