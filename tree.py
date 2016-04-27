class ObjectItem(object):
	"""docstring for ObjectItem"""
	def __init__(self,arg=None):
		super(ObjectItem, self).__init__()
		self.__value = arg


	def setVal(self,val):
		if self.__type is None:
			self.__type = type(val)
		else:
			if self.__type != type(val):
				raise TypeError
			else:
				self.__value = val

	def getVal(self):
		return self.__value

	def setLeft(self,left):
		self.__left = left

	def getLeft(self):
		return self.__left

	def setRight(self,right):
		self.__right = right

	def getRight(self):
		return self.__right

	__value = None
	__left = None
	__right = None


class BinaryTree(object):
	"""docstring for Tree"""
	def __init__(self):
		super(BinaryTree, self).__init__()

	def size(self):
		return self.__count
    
	def isEmpty(self):
		if self.__count>0:
			return False
		else:
			return True
    
	def contains(self,element):
		pass
    
	def removeLeftSubtree(self):
		pass
	
	def removeRightSubtree(self):
		pass
	
	def find(self,targetelement):
		pass
	
	def toString(self):
		pass
	
	def preInorder(self,arrow):
		if not arrow is None:
			self.__preString = self.__preString + arrow.getVal()
			self.preInorder(arrow.getLeft())
			self.preInorder(arrow.getRight())
			return self.__preString
		
	def postInorder(self,arrow):
		if not arrow is None:
			self.postInorder(arrow.getLeft())
			self.postInorder(arrow.getRight())
			self.__postString = self.__postString + arrow.getVal()
			return self.__postString

	def inOrder(self,arrow):
		if not arrow is None:
			self.inOrder(arrow.getLeft())
			self.__inString = self.__inString + arrow.getVal()
			self.inOrder(arrow.getRight())
			return self.__inString

	def create(self):
		print("Please input the value")
		val = raw_input()
		item = ObjectItem(val)
		if not self.__root is None:
			self.__root = item
		print("If the node "+str(val)+" has left child?")
		isLeft = raw_input()
		if isLeft == "y" or isLeft == "Y":
			item.setLeft(self.create())
		print("If the node "+str(val)+" has right child?")
		isRight = raw_input()
		if isRight == "y" or isRight == "Y":
			item.setRight(self.create())
		return item

	def getRoot(self):
		return self.__root

	def setRoot(self,root):
		self.__root = root

	__count = 0
	__root = None
	__preString = ''
	__postString = ''
	__inString = ''

tree = BinaryTree()
tree.setRoot(tree.create())
print(tree.preInorder(tree.getRoot()))
		