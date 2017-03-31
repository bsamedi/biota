import string

def dnaPalindromes(sequence):
    reversed = sequence[::-1].translate(string.maketrans('ATGC','TACG'))
    searcher = SubsequenceIndex(reversed)
    for i in range(len(sequence)):
        for res in searcher.find(sequence[i:]):
            yield res

class SubsequenceIndex():
    def __init__(self, str):
        self.searchIn = str
        self.root = IndexNode()
        self.root.positions = set(range(len(self.searchIn)))
    
    # Find any number of leading characters from "what" in the string provided at instance creation
    def find(self, what):
        for start, end in self.findByNodes(self.root, what, 0):
            yield self.searchIn[start:end]
    
    def findByNodes(self, nodeThis, what, lengthFound):
        positions = []
        if len(what) == 0 and lengthFound > 0:
            positions += nodeThis.positionsWithChildren()
        
        elif len(what) > 0:
            nodeNext = self.getChild(nodeThis, what[0] )
        
        return positions

    def getChild(self, node, key):
        if not key in node.children:
            self.buildChild(node, key)

        return node.children[key]
    
    def buildChild(self, node, key):
        pass
    
    def positionsWithChildren(self):
        return self.position + [ i-1 for i in [child.positionsWithChildren() for child in self.children.itervalues() if child != None ]]

class IndexNode():
    def __init__(self):
        self.positions = set()
        self.children = {}
