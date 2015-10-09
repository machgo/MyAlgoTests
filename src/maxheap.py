#!/usr/bin/python
from random import randint

class item:
    key = 0
    value = 0
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __str__(self):
        return str(self.value)

def get_parent(pos):
    return (pos-1)/2

def left(pos):
    return pos*2+1

def right(pos):
    return left(pos)+1

def upheap(data, pos):
    if pos == 0:
        return 

    if data[pos] > data[get_parent(pos)]:
        temp = data[pos]
        data[pos] = data[get_parent(pos)]
        data[get_parent(pos)] = temp
        tpos = data[pos].key
        data[pos].key = data[get_parent(pos)].key
        data[get_parent(pos)].key = tpos
        upheap(data, get_parent(pos))

def downheap(data,pos):
    if pos > len(data)-1:
        return
    biggest = 0
    if left(pos) <= len(data)-1:
        biggest = left(pos)
        if right(pos) <= len(data)-1:
            if data[biggest] < data[right(pos)]:
                biggest = right(pos)
        if data[biggest] > data[pos]:
            temp = data[pos]
            data[pos] = data[biggest]
            data[biggest] = temp
            tpos = data[pos].key
            data[pos].key = data[biggest].key
            data[biggest].key = tpos
            downheap(data,biggest)

def heapCheck(data):
    for i in range(0,len(data)):
        if i != 0:
            if data[i] > data[get_parent(i)]:
                return False
    return True

def heapify(data):
    pos = 0
    while heapCheck(data) != True:
        for i in range(0,len(data)):
            downheap(data,i)
        pos+=1

def heapSort(data):
    result = [0] * len(data)
    tempdata = list(data)
    for i in range(0,len(data)):
        heapify(tempdata)
        pos = len(data)-1-i
        result[pos] = tempdata[0]
        tempdata[0] = tempdata[pos]
        tempdata = tempdata[:pos]
    return result

def printTree(data):
    level = 0
    onlevel = 0
    for i in range(0,len(data)):
        print(data[i]),
        onlevel+=1
        
        if onlevel == (2**level):
            level+=1
            onlevel=0
            print
        elif i == 0:
            level+=1
            onlevel=0
            print
    print

def insert(data, value):
    i = item()
    i.key = len(data)
    i.value = value
    data.append(i)
    upheap(data,i.key)
    downheap(data,i.key)
    return i

if __name__ == "__main__":
    print "maxheap example"

data = []
for i in range(0,999):
    insert(data,randint(0,9999));

printTree(data)
insert(data,444)
printTree(data)

print printTree(heapSort(data))

