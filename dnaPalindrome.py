import string
from collections import namedtuple

def dnaPalindromes(sequence):
    reversed = sequence[::-1].translate(string.maketrans('ATGC','TACG'))
    searcher = SubsequenceIndex(reversed)
    for i in range(len(sequence)):
        for res in searcher.find(sequence[i:]):
            yield res
"""
    Search algorithm is as follows:
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
        self.searchIn = str
        self.root = IndexNode()
        self.root.positions = set(range(len(self.searchIn)))

    # Find any number of leading characters from "what" in the string provided at instance creation
    def find(self, what):
        for start, end in self.findByNodes(self.root, what, 0):
            yield self.searchIn[start:end]

    def findByNode(self, nodeThis, what, whatIndex):
        positions = []
        if len(what) == 0 and lengthFound > 0:
            positions += nodeThis.positionsWithChildren()

        elif len(what) > 0:
            nodeNext = self.getChild(nodeThis, what[0] )

        return positions

    def buildChild(self, node, key):
        pass

    def positionsWithChildren(self):
        return self.position + [ i-1 for i in [child.positionsWithChildren() for child in self.children.itervalues() if child != None ]]

class IndexNode(namedtuple('IndexNode', 'children, positions')):
    class DEAD_END:
        pass

    @staticmethod
    def new():
        return IndexNode(positions = set(), children = {})

    @staticmethod
    def isDeadEnd(node):
        return node == IndexNode.DEAD_END

    @staticmethod
    def isNode(node):
        return isinstance(node, IndexNode)

    def childExists(self, key):
        return key in self.children

    def getChild(self, key):
        return self.children[key]

    def addChild(self, key, addresses):
        if len(addresses) > 0:
            self.children[key] = IndexNode(children = {}, positions = addresses)
        else:
            self.children[key] = IndexNode.DEAD_END

    def positionsIncludinChildren(self):
        all = self.positions
        for child in self.children.values():
            for pos in child.positionsIncludinChildren():
                all.add(pos-1)
        return all
