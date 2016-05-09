import math


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
                # self.add_element(x)
                self.add_element_ary(x)

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

    def add_element_ary(self, val=None):
        self.heap_ary.append(val)
        self.reorder()

    def pre_in_order(self, arrow):
        if arrow is self.root:
            del self.pre_string[:]
        if arrow is not None:
            self.pre_string.append(arrow.val)
            self.pre_in_order(arrow.left)
            self.pre_in_order(arrow.right)
            return self.pre_string

    def find_min(self):
        self.reorder()
        return self.heap_ary[0]

    def remove_min(self):
        self.heap_ary[0] = self.heap_ary[len(self.heap_ary)-1]
        self.heap_ary.pop()
        

    def reorder(self):
        length = len(self.heap_ary)
        if length > 0:
            layer = int(math.log(length, 2))  # calculate the layer from 0 layer
            cont = int(math.pow(2, layer + 1) - 2)
            while cont >= 0:
                if cont * 2 + 1 > length - 1:
                    cont -= 1
                else:
                    self.heap_reorder(cont, length)
                    cont -= 1

    def heap_reorder(self, rp, length):
        lchild = 2 * rp + 1
        rchild = 2 * rp + 2
        if lchild <= length - 1:
            if rchild <= length - 1:
                if self.heap_ary[lchild] <= self.heap_ary[rchild]:
                    if self.heap_ary[lchild] < self.heap_ary[rp]:
                        tmp = self.heap_ary[lchild]
                        self.heap_ary[lchild] = self.heap_ary[rp]
                        self.heap_ary[rp] = tmp
                        self.heap_reorder(lchild, length)
                    else:
                        return None
                else:
                    if self.heap_ary[rchild] < self.heap_ary[rp]:
                        tmp = self.heap_ary[rchild]
                        self.heap_ary[rchild] = self.heap_ary[rp]
                        self.heap_ary[rp] = tmp
                        self.heap_reorder(rchild, length)
                    else:
                        return None
            else:
                if self.heap_ary[lchild] < self.heap_ary[rp]:
                    tmp = self.heap_ary[lchild]
                    self.heap_ary[lchild] = self.heap_ary[rp]
                    self.heap_ary[rp] = tmp
                    self.heap_reorder(lchild, length)
        else:
            return None

    root = None
    last_node = None
    pre_string = []
    heap_ary = []


tree = Heap([28, 10, 30, 5, 9, 15, 12, 22, 18, 13, 27, 1])
tree.reorder()
print (tree.heap_ary)
