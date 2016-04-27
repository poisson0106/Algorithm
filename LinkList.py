class ObjectItem(object):
	"""docstring for ObjectItem"""
	def __init__(self):
		super(ObjectItem, self).__init__()
		
	def setVal(val):
		if self.__type is None:
			self.__type = type(val)
		else:
			if self.__type != type(val):
				raise TypeError
			else:
				self.__value = val

	def getVal(val):
		return self.__value

	def setNext(next):
		self.__next = next

	def getNext():
		return self.__next 

	__value = None
	__next = None
	__type = None
		

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		super(LinkedList, self).__init__()
		head = ObjectItem()

	head = None





		