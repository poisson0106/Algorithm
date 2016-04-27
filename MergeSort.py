def mergeSort(list):
	if len(list)<=1:
		return list
	mid = len(list) / 2
	left = mergeSort(list[:mid])
	right = mergeSort(list[mid:])
	return merge(left,right)

def merge(left,right):
	target = []
	i = 0
	j = 0

	while i != len(left) and j != len(right):
		if left[i]>=right[j]:
			target.append(left[i])
			i +=1
		else:
			target.append(right[j])
			j +=1

	if i == len(left) and j != len(right):
		target.extend(right[j:])
	elif j == len(right) and i != len(left):
		target.extend(left[i:])

	return target

ary=[15,3,30,21,10,33,18,28,1]
print(mergeSort(ary))
