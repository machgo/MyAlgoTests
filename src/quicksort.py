#!/usr/bin/python
from random import randint
import time

def quickSelect(data,number):
    quickSelectHelper(data,number,0,len(data)-1)

def quickSelectHelper(data,number,first,last):
    pivot = partition(data,first,last)
    if (number == pivot):
        return data[pivot]
    elif (number < pivot):
        return quickSelectHelper(data,number,first,pivot-1)
    else:
        return quickSelectHelper(data,number,pivot+1, last)

def quickSort(data):
    quickSortHelper(data,0,len(data)-1)

def quickSortHelper(data,first,last):
    if first<last:
        splitpoint = partition(data,first,last)
       	quickSortHelper(data,first,splitpoint-1)
       	quickSortHelper(data,splitpoint+1,last)

def partition(data,first,last):
    pivotvalue = data[last]

    leftmark = first
    rightmark = last-1

    done = False
    while not done:
        #print "data: {}".format(data[first:last])
        #print "pivot: {}".format(pivotvalue)
        #until bigger value than pivot found or end of array
        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
	    leftmark = leftmark + 1

        #until smaller value than pivot found or beginning of array
        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        #everything's sorted
        if rightmark < leftmark:
            done = True

        #swap places
        else:
	    temp = data[leftmark]
	    data[leftmark] = data[rightmark]
	    data[rightmark] = temp
    #move pivot to correct position
    temp = data[last]
    data[last] = data[leftmark]
    data[leftmark] = temp
    return leftmark

alist = []
for i in range(1,10):
    alist.append(randint(1,20))

startTime = time.time()
#quickSort(alist)
#print(alist)

print alist
quickSelect(alist,3)
print alist

exeTime = time.time() - startTime
print "execution time: {}".format(exeTime)

