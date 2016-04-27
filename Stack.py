class typeMistake(ValueError):
	pass
		

class StackTmp(object):
	"""docstring for StackTmp"""
	def __init__(self,ary=None):
		super(StackTmp, self).__init__()
		if not ary is None:
			self.__type = type(ary[0])
			for x in ary[1:]:
				if type(x) !=self.__type:
					raise typeMistake("The array's type isn't same")
			self.__ary = ary
			self.__count = len(ary)
		
	__type = None
	__count = 0
	__ary = []

	def pushStack(self,element):
		if self.__count == 0:
			self.__type = type(element)
		else:
			if self.__type != type(element):
				raise typeMistake("This element type isn't the same as the first one")
		self.__ary.append(element)
		self.__count +=1

	def pullStack(self):
		self.__count -=1
		tmp = self.__ary[self.__count]
		del self.__ary[self.__count]
		return tmp

	def popStack(self):
		return self.__ary[self.__count-1]

	def stackSize(self):
		return self.__count

	def toString(self):
		tmp =''
		for x in self.__ary:
			tmp = tmp+str(x)

		return tmp

a = StackTmp([1,2])
a.pushStack('6')
print(a.stackSize())
print(a.pullStack())
print(a.popStack())
print(a.toString())

