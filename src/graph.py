#!/usr/bin/python

class vertex:
    value = 0
    d = 0
    source = None
    edges = None
    def __str__(self):
        return str(self.value)
    def __init__(self, value):
        self.value = value

class edge:
    v1 = None
    v2 = None
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

def getAdjecents(v):
    result = []
    for i in edges:
        if i.v1 is v:
            result.append(i.v2)
        if i.v2 is v:
            result.append(i.v1)
    return result

def resetDecoration():
    for i in vertexes:
        i.d = 0 
        i.source = 0

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
        print i.value
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
        
vertexes = []
edges = []
vertexes.append(vertex(1))
vertexes.append(vertex(2))
vertexes.append(vertex(3))
vertexes.append(vertex(4))
vertexes.append(vertex(5))
vertexes.append(vertex(6))
edges.append(edge(vertexes[0],vertexes[1]))
edges.append(edge(vertexes[0],vertexes[2]))
edges.append(edge(vertexes[1],vertexes[3]))
edges.append(edge(vertexes[1],vertexes[4]))
edges.append(edge(vertexes[2],vertexes[3]))
edges.append(edge(vertexes[3],vertexes[4]))
edges.append(edge(vertexes[3],vertexes[5]))

#visitAll()
#bfs()
#shortestPath(vertexes[0],vertexes[4])

print findComponents()
vertexes.append(vertex(7))
print findComponents()
edges.append(edge(vertexes[5],vertexes[6]))
print findComponents()
