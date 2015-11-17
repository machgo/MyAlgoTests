#!/usr/bin/python

from random import randint

alist = []
for i in range(0,100):
    alist.append(randint(1,99))

buckets = []
for i in range(0,10):
    buckets.append([])

for i in range(0,99):
    pos = alist[i]/10
    buckets[pos].append(alist[i])

print alist
print buckets

