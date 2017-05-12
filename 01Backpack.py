class Item(object):
    def __init__(self, val, weight):
        super(Item, self).__init__()
        self.val = val
        self.weight = weight
    val = 0
    weight = 0

weight = [2, 2, 6, 5, 4]
val = [6, 3, 5, 4, 6]
allWeight = 10
count = 5

items = []

# In weight 0 package status
lastMax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
formerMax = []

#Init items
for i in range(count):
    items.append(Item(val[i], weight[i]))

for item in items:
    formerMax = lastMax[:]
    for w in range(1, allWeight+1):
        if items.index(item) == 0:
            if w-item.weight >= 0:
                lastMax[w] = item.val
        else:
            formerWeight = w - item.weight
            if formerWeight >= 0:
                if formerMax[formerWeight]+item.val > formerMax[w]:
                    lastMax[w] = formerMax[formerWeight]+item.val
                else:
                    continue
            else:
                continue

print(lastMax)
