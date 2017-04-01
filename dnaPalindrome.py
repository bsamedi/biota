import string
from collections import namedtuple

def dnaPalindromes(sequence):
    reversed = sequence[::-1].translate(string.maketrans('ATGC','TACG'))
    searcher = SubsequenceIndex(reversed)
    for i in range(len(sequence)):
        for res in searcher.find(sequence[i:]):
            yield res
"""
    Search algorithm:
        initially there is the root node with no children and all Where to search list positions
    Search request:
        let current node be the root
        for What to search position in 0 .. What to search length:
            if node does not have child, build it:
                for every address in current node positions:
                    if Where to search[ address ] equals current What to search:
                        add address to the Found list
                add child with Found list, optionally empty
            Get child for What to search
            If child is DEAD END:
                return What to search[ 0 .. current position ], with recursive addresses of this node and all its children
            else:
                set Current node to be the Child
"""

class SubsequenceIndex():
    def __init__(self, str):
        self.where = str
        self.root = IndexNode.new()
        self.root.positions.update(range(len(self.where)))

    # Find any number of leading characters from "what" in the string provided at instance creation
    def find(self, what, minLength=1):
        node = self.root
        lastFoundNode = None
        for iWhat in range(len(what)):
            nextNode = self.getChild(node, what[iWhat])
            if IndexNode.isDeadEnd(nextNode):
                break
            else:
                yield (what[0:iWhat+1], nextNode.positionsIncludingChildren())
            node = nextNode

    def getChild(self, node, key):
        if node.childExists(key):
            child = node.getChild(key)
        else:
            foundPositions = set()
            for iWhere in node.positions:
                if self.where[iWhere] == key:
                    foundPositions.add(iWhere)

            child = node.addChild(key, foundPositions)
            node.positions.difference_update(foundPositions)
        return child

class IndexNode(namedtuple('IndexNode', 'children, positions')):
    @staticmethod
    def new():
        return IndexNode(positions = set(), children = {})

    @staticmethod
    def isDeadEnd(node):
        return node == None

    @staticmethod
    def isNode(node):
        return isinstance(node, IndexNode)

    def childExists(self, key):
        return key in self.children

    def getChild(self, key):
        return self.children[key]

    def addChild(self, key, addresses):
        if len(addresses) > 0:
            newNode = IndexNode(children = {}, positions = addresses)
        else:
            newNode = None
        self.children[key] = newNode
        return newNode

    def positionsIncludingChildren(self):
        all = set()
        all |= self.positions
        for child in self.children.values():
            if not IndexNode.isDeadEnd(child):
                all |= child.positionsIncludingChildren()
        return all
