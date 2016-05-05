class ObjectItem(object):
    """docstring for ObjectItem"""

    def __init__(self, arg=None):
        super(ObjectItem, self).__init__()
        self.__value = arg

    def setVal(self, val):
        self.__value = val

    def getVal(self):
        return self.__value

    def setLeft(self, left):
        self.__left = left

    def getLeft(self):
        return self.__left

    def setRight(self, right):
        self.__right = right

    def getRight(self):
        return self.__right

    __value = None
    __left = None
    __right = None
    __type = None


class BinaryTree(object):
    """docstring for Tree"""

    def __init__(self):
        super(BinaryTree, self).__init__()

    def size(self):
        return self.__count

    def isEmpty(self):
        if self.__count > 0:
            return False
        else:
            return True

    def removeLeftSubtree(self, arrow=None):
        if arrow is not None and arrow is not self.__root.getRight():
            del self.__preString[:]

            self.removeLeftSubtree(arrow.getLeft())
            self.removeLeftSubtree(arrow.getRight())
            print(arrow.getVal())
            if arrow is self.__root:
                arrow.setLeft(None)
            else:
                arrow.setLeft(None)
                arrow.setRight(None)
                arrow = None

    def removeRightSubtree(self, arrow=None):
        if arrow is not None and arrow is not self.__root.getLeft():
            del self.__preString[:]

            self.removeLeftSubtree(arrow.getRight())
            self.removeLeftSubtree(arrow.getLeft())
            print(arrow.getVal())
            if arrow is self.__root:
                arrow.setRight(None)
            else:
                arrow.setLeft(None)
                arrow.setRight(None)
                arrow = None

    def find(self, arrow, val):
        if arrow is not None:
            if arrow.getVal() == val:
                return arrow
            else:
                l = self.find(arrow.getLeft(), val)
                if l is not None:
                    return l
                r = self.find(arrow.getRight(), val)
                if r is not None:
                    return r
                return None

    def toString(self):
        pass

    def preInorder(self, arrow):
        if arrow is not None:
            self.__preString.append(arrow.getVal())
            self.preInorder(arrow.getLeft())
            self.preInorder(arrow.getRight())
            return self.__preString

    def postInorder(self, arrow):
        if arrow is not None:
            self.postInorder(arrow.getLeft())
            self.postInorder(arrow.getRight())
            self.__postString.append(arrow.getVal())
            return self.__postString

    def inOrder(self, arrow):
        if arrow is not None:
            self.inOrder(arrow.getLeft())
            self.__inString.append(arrow.getVal())
            self.inOrder(arrow.getRight())
            return self.__inString

    def levelOrder(self):
        queue = []
        if self.getRoot() is not None:
            queue.append(self.getRoot())
            parent_count = 1
            child_count = 0
            while len(queue) != 0:
                head = queue[0]
                if head.getLeft() is not None:
                    queue.append(head.getLeft())
                    child_count += 1
                if head.getRight() is not None:
                    queue.append(head.getRight())
                    child_count += 1
                print head.getVal(),
                queue.pop(0)
                parent_count -= 1

                if parent_count == 0:
                    parent_count = child_count
                    child_count = 0
                    print ("----------------------------")


    def create(self):
        print("Please input the value")
        val = raw_input()
        item = ObjectItem(val)
        if self.__root is not None:
            self.__root = item
        print("If the node " + str(val) + " has left child?")
        isLeft = raw_input()
        if isLeft == "y" or isLeft == "Y":
            item.setLeft(self.create())
        print("If the node " + str(val) + " has right child?")
        isRight = raw_input()
        if isRight == "y" or isRight == "Y":
            item.setRight(self.create())
        return item

    def getRoot(self):
        return self.__root

    def setRoot(self, root):
        self.__root = root

    __count = 0
    __root = None
    __preString = []
    __postString = []
    __inString = []


tree = BinaryTree()
tree.setRoot(tree.create())
tree.levelOrder()
# print(tree.preInorder(tree.getRoot()))
# tree.removeLeftSubtree(tree.getRoot())
# print(tree.preInorder(tree.getRoot()))
# tree.removeRightSubtree(tree.getRoot())
# print (tree.preInorder(tree.getRoot()))
