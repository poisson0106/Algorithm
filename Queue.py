class typeException(Exception):
	pass
		

class QueueTmp(object):
	"""docstring for QueueTmp"""
	def __init__(self):
		super(QueueTmp, self).__init__()
	
	__ary = []
	__count = 0
	__type = None

	def enQueue(self,element):
		if self.__count==0:
			self.__type = type(element)
			self.__ary.append(element)
			self.__count +=1
		else:
			if self.__type != type(element):
				raise typeException
			else:
				self.__ary.append(element)
				self.__count +=1

	def deQueue(self):
		if self.__count==0:
			raise Exception
		else:
			tmp = self.__ary[0]
			self.__count -=1
			del self.__ary[0]
			return tmp

	def first(self):
		return self.__ary[0]

	def isEmpty(self):
		if self.__count==0:
			return True
		else:
			return False

	def size(self):
		return self.__count

	def toString(self):
		tmp = ''
		for x in self.__ary:
			tmp = tmp + str(x)
		return tmp

a = QueueTmp()
a.enQueue(3)
a.enQueue(4)
a.deQueue()
print(a.first())
print(a.toString())