#!/usr/bin/python
class item:
    value = 0
    left = None
    right = None
    down = None
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __str__(self):
        return str(self.value)
    def __init__(self, value):
        self.value = value

height = 2
topLeft = item (-2)
bottomLeft = item (-3)

topLeft.down = bottomLeft

def shouldI():
    if random.randint(0,10) < 7:
        return False
    else:
        return True

def search(value):
    item = topLeft
    for i in range(1,height):
        while item.right is not None and item.right.Value < value:
            item = item.right
        item = item.down
    return item



def insert (value):
    befI = search(value)
    aftI = befI.right
    befI.right = item(value)
    befI.right.left = befI
    if aftI is not None:
        befI.right.right = aftI
        aftI.left = befI.right



    


insert(22)
insert(33)
insert(44)

i = bottomLeft 
while i is not None:
    print i.value
    i = i.right

