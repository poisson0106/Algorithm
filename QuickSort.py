def leftSort(left,right,tag):
	global ary
	while left!=0 and left!=right:
		if ary[left]>tag:
			ary[right] = ary[left]
			right -= 1
			break
		else:
			left += 1
	if left!=right:
		return rightSort(left,right,tag)
	else:
		ary[right] = tag
		return right
	


def rightSort(left,right,tag):
	global ary
	while right!=0 and left!=right:
		if ary[right]<tag:
			ary[left] = ary[right]
			left += 1
			break
		else:
			right -= 1
	if left!=right:
		return leftSort(left,right,tag)
	else:
		ary[left] = tag
		return left

def sortAry(left,right,tag):
	global ary
	if left!=right:
		mid = rightSort(left, right, tag)
		if mid!=left:
			sortAry(left,mid-1,ary[0]) #Middle left part sort
		if mid!=right:
			sortAry(mid+1,right,ary[mid+1]) #Middle right part sort


ary = [28,12,34,3,45,67,36,47]

if len(ary)!=0:
	sortAry(0,len(ary)-1,ary[0])
	print(ary)
else:
	print("The array is empty")