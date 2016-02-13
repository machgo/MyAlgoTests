#!/usr/bin/python

class vertex:
    value = 0
    d = 0
    inDegree = 0
    number = 0
    source = None
    edges = None
    def __str__(self):
        return "value: {}, number: {}".format(self.value,self.number)
    def __init__(self, value):
        self.value = value

class edge:
    start = None
    to = None
    weight = 1 
    def __init__(self, start, to, weight=1):
        self.start = start
        self.to = to
        self.weight = weight

def getAdjecents(v):
    result = []
    for i in edges:
        if i.start is v:
            result.append(i.to)
    return result

def resetDecoration():
    for i in vertexes:
        i.d = 0 
        i.source = 0
        i.number = 0
        i.inDegree = 0

def goNext(v):
    v.d = 1
    nodes = getAdjecents(v)
    for i in nodes:
        if i.d == 0:
            goNext(i)

def visitAll():
    resetDecoration()
    goNext(vertexes[0])

def findComponents():
    resetDecoration()
    result=0

    for i in vertexes:
        if i.d == 0:
            goNext(i)
            result+=1

    return result

def bfs():
    resetDecoration()
    start = vertexes[0]
    start.d = 1
    ns = []
    ns.append(start)
    while len(ns) > 0:
        i = ns.pop(0)
        print i
        tmp = getAdjecents(i)
        for b in tmp:
            if b.d == 0:
                b.d = 1
                ns.append(b)

def shortestPath(start, end):
    resetDecoration()
    start.d = 1
    ns = []
    ns.append(start)
    i = start
    while len(ns) > 0:
        i = ns.pop(0)
        tmp = getAdjecents(i)
        if i is end:
            break
        for b in tmp:
            if b.d == 0:
                b.d = 1
                b.source = i
                ns.append(b)

    while i is not start:
        print i.value
        i = i.source
    print i.value

def getInDegree(node):
    i = 0
    for x in edges:
        if x.to is node:
            i+=1
    return i

def topoNumbering():
    s = []
    i = 0
    for v in vertexes:
       v.inDegree = getInDegree(v)
       if v.inDegree == 0:
           s.append(v)
           print "starting object: {}".format(v.value)
    while len(s) > 0:
        item = s.pop(0)
        print "looking at object: {}".format(item.value)
        item.number = i
        i+=1
        for e in edges:
            if e.start is item:
                e.to.inDegree-=1
                if e.to.inDegree == 0:
                    print "{} has now 0 inDegree".format(e.to.value)
                    s.append(e.to)

def allShortestPath():
    s = []
        
vertexes = []
edges = []
vertexes.append(vertex(1))
vertexes.append(vertex(2))
vertexes.append(vertex(3))
vertexes.append(vertex(4))
vertexes.append(vertex(5))
vertexes.append(vertex(6))
vertexes.append(vertex(7))
vertexes.append(vertex(8))
vertexes.append(vertex(9))
edges.append(edge(vertexes[0],vertexes[3]))
edges.append(edge(vertexes[0],vertexes[4]))
edges.append(edge(vertexes[1],vertexes[2]))
edges.append(edge(vertexes[1],vertexes[3]))
edges.append(edge(vertexes[2],vertexes[3]))
edges.append(edge(vertexes[2],vertexes[5]))
edges.append(edge(vertexes[2],vertexes[7]))
edges.append(edge(vertexes[3],vertexes[4]))
edges.append(edge(vertexes[4],vertexes[6]))
edges.append(edge(vertexes[4],vertexes[8]))
edges.append(edge(vertexes[5],vertexes[6]))
edges.append(edge(vertexes[6],vertexes[8]))
edges.append(edge(vertexes[7],vertexes[8]))

#visitAll()
#shortestPath(vertexes[0],vertexes[4])
topoNumbering()

for v in sorted(vertexes, key=lambda vertex: vertex.number):
    print v

#print findComponents()
#vertexes.append(vertex(7))
#print findComponents()
#edges.append(edge(vertexes[5],vertexes[6]))
