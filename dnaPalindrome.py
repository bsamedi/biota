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
        for i in self.findByNodes(self.root, what):
            yield self.searchIn[i]
    
    def findByNodes(self, nodeThis, what):
        positions = []
        if len(what) > 0:
            what0 = what[0]
            if what0 in nodeThis.children:
                nodeNext = nodeThis.children[what0]
            else:
                # calculate child node
                found = set([ i for i in nodeThis.positions if self.searchIn[i]==what0 ])
                if len(found)>0:
                    nodeNext = IndexNode()
                    nodeNext.positions = found
                    nodeThis.positions -= found
                else:
                    nodeNext = None
                nodeThis.children[what0] = nodeNext
            if nodeNext != None:
                for i in nodeNext.positions:
                    yield i
                self.findByNodes(nodeNext, what[1:])

class IndexNode():
    def __init__(self):
        self.positions = set()
        self.children = {}
