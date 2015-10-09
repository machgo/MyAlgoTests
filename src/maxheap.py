#!/usr/bin/python
from random import randint

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
    for i in range(0,len(data)):
        print(data[i]),
        
        if i+1 == (2^level):
            level+=1
            print
        elif i == 0:
            level+=1
            print

if __name__ == "__main__":
    print "maxheap example"

data = []
data.append(1)
for i in range(0,1024):
    data.append(randint(0,99999))

heapify(data)

printTree(data)
print heapSort(data)

