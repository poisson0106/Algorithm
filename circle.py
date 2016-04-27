class People(object):
    """docstring for People"""

    def __init__(self, num, nextobj):
        super(People, self).__init__()
        self.num = num
        self.nextobj = nextobj

N = 3
n = 2
isContinue = True
head = None
previous = None
count = N
current = None

def removeOne(step):
	global current
	for x in xrange(step-1):
		current = current.nextobj
	
	tmpPerson = current.nextobj
	current.num = tmpPerson.num
	current.nextobj = tmpPerson.nextobj
	del tmpPerson


for x in xrange(N):
    if x == 0:
        head = People(x + 1, None)
        previous = head
    else:
        tmp = People(x + 1, None)
        previous.nextobj = tmp
        previous = tmp

previous.nextobj = head
current = head
    
while count>1:
	if count<n:
		remain = n % count
		removeOne(remain)
		count -= 1
	else:
		removeOne(n)
		count -= 1
        
print(current.num)
