#!/usr/bin/python
from random import randint

class item:
    key = 0
    value = 0
    height = 0
    left = None
    right = None
    parent = None
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __str__(self):
        return str(self.value)
    def __init__(self, value):
        self.value = value
    def isExternal(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

def printTree(root):
    level = 0
    data = []
    data.append([root])
    going = True
    while going:
        data.append([])
        going = False
        for n in data[level]:
            if n.left is not None:
                going = True
                data[level+1].append(n.left)
            if n.right is not None:
                going = True
                data[level+1].append(n.right)
        level+=1

    for l in data:
        text = ""
        for i in l:
            text += str(i.value)
            text += " h:"
            text += str(i.height)
            text += " "
        print text

def compare(node,value):
    if node.value > value:
        return True
    else:
        return False

def insert(root, value):
    pos = 0
    node = root
    going = True

    
    while going:
        if node.left is None and value < node.value:
            node.left = item(value)
            node.left.parent = node
            updateHeight(node.left)
            going = False
        elif node.right is None and value >= node.value:
            node.right = item(value)
            node.right.parent = node
            updateHeight(node.right)
            going = False
        else:
            if node.left.value > value:
                node = node.left
            else:
                node = node.right

def smallest(root):
    going = True
    node = root
    while going:
        if node.left is None:
            return node
        else:
            node = node.left
    return node

def biggest(root):
    going = True
    node = root
    while going:
        if node.right is None:
            return node
        else:
            node = node.right
    return node

def next(root):
    if root.right is None:
        if root.parent.left is root:
            return root.parent
        else:
            while root.parent is not None and root == root.parent.right:
                root = root.parent
    else:
        return smallest(root.right)

def treeWalk(root):
    if root is not None:
        treeWalk(root.left)
        print root.value
        treeWalk(root.right)

def iterate (root):
    node = smallest(root)
    while node is not None:
        print str(node)
        node = next(node)

def closestBefore(root, key):
    if root.value == key:
        return root
    temp = root
    while temp is not None:
        before = temp
        if temp.value < key:
            temp = temp.left
        else:
            temp = temp.right
        temp = next(temp)
    return before
        
        


def updateHeight(root):
    h = 0
    while root is not None:
        if root.height < h:
            root.height = h
        root = root.parent
        h+=1

def testTree(root):
    if root is None:
        return
    testTree(root.left)
    testTree(root.right)
    if root.left is not None:
        if root.left.parent is not root:
            print "error"
    if root.right is not None:
        if root.right.parent is not root:
            print "error"

def replace_node_in_parent(node, new_value=None):
    if node.parent:
        if node == node.parent.left:
            node.parent.left = new_value
        else:
            node.parent.right = new_value
    if new_value:
        new_value.parent = node.parent

def remove(toRemove):
    if toRemove.left is None and toRemove.right is not None:
        replace_node_in_parent(toRemove.right)
    elif toRemove.right is None and toRemove.left is not None:
        replace_node_in_parent(toRemove.left)

    elif toRemove.left is not None and toRemove.right is not None:
        r = smallest(toRemove.right) #find leftest in right Subtree
        print "replacement has value: %d" % r.value
        toRemove.value = r.value
        remove(r)
    else:
        replace_node_in_parent(toRemove)

if __name__ == "__main__":
    print "binary tree example"

root = item(1000)
insert(root,999)
insert(root,777)
insert(root,666)
insert(root,1111)
insert(root,1222)
insert(root,1050)
printTree(root)
#for i in range(0,16):
#    insert(root,randint(0,9999));
remove(root.left)
printTree(root)
print "smallest number is: %d" % smallest(root).value
print "biggest number is: %d" % biggest(root).value

iterate(root)
treeWalk(root)
print closestBefore(root,1111)

