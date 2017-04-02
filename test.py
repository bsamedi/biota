#!/usr/bin/env python
import unittest
import mock
from mock import patch
from mock import Mock

from dnaPalindrome import IndexNode

class testChildOps(unittest.TestCase):
    def testNewIndexNode(self):
        i = IndexNode.new()
        self.assertEqual(i.positions, set())
        self.assertEqual(i.children, {})

    def testChildNotExists(self):
        i = IndexNode.new()
        self.assertEquals(i.childExists('a'), False)

    def testChildExists(self):
        i = IndexNode.new()
        i.addChild('a', set([1, 2, 3]))
        self.assertEquals(i.childExists('a'), True)

    def testGetChild(self):
        i = IndexNode.new()
        i.addChild('c', set([1,2,3]))
        node = i.getChild('c')
        self.assertEqual(node.children, {})
        self.assertEqual(node.positions, set([1,2,3]))

    def testDeadEnd(self):
        i = IndexNode.new()
        i.addChild('b', set())
        node = i.getChild('b')
        self.assertEquals(IndexNode.isDeadEnd(node), True)

    def testositionsRecursive0(self):
        i = IndexNode.new()
        self.assertEquals(i.positionsIncludingChildren(), set([]))

    def testositionsRecursive1(self):
        root = IndexNode.new()
        root.addChild('42', set([2,3,42]))
        i = root.getChild('42')
        self.assertEquals(i.positionsIncludingChildren(), set([2,3,42]))

    def testositionsRecursive2(self):
        root = IndexNode.new()
        root.addChild('42', set([2,3,42]))
        i = root.getChild('42')
        i.addChild('T', set([17, 26]))
        self.assertEquals(
            set( root.positionsIncludingChildren() ),
            set([2,3,42,17,26]))

    def testositionsRecursive3(self):
        root = IndexNode.new()
        root.addChild('42', set([2,3,42]))
        root.addChild('bravo', set([3, 100, 42]))
        i = root.getChild('42')
        i.addChild('T', set([4, 17, 26]))
        found = root.positionsIncludingChildren()
        expected = set([2,3,42, 3,100,42,4, 17, 26])
        self.assertEquals(found, expected)

    def testositionsRecursive_Twice(self):
        root = IndexNode.new()
        root.addChild('A', set([1]))
        root.addChild('B', set([4]))
        self.assertEquals(len(root.positions), 0)
        root.positionsIncludingChildren()
        found = root.positionsIncludingChildren()
        self.assertEquals(len(root.positions), 0)

from dnaPalindrome import SubsequenceIndex

class testSequenceIndex(unittest.TestCase):
    def test1(self):
        ix = SubsequenceIndex('abc')
        found = list(ix.find('a'))
        self.assertEqual( found,
            [ ('a', set([0])) ] )

    def test2(self):
        ix = SubsequenceIndex('abcd')
        found = list(ix.find('bc'))
        self.assertEqual(found,
            [ ('bc', set([1])) ] )

    def test3(self):
        ix = SubsequenceIndex('abc')
        found = list(ix.find('defg'))
        self.assertEqual(found, list())

    def test4(self):
        ix = SubsequenceIndex('xABCD')
        found = list( ix.find('ABCD') )
        expected = [
            ('ABCD', set([1])) ]
        self.assertEqual(found, expected)

    def test5(self):
        ix = SubsequenceIndex('ABCABDABC')
        found = list( ix.find('ABC') )
        expected = [
            ('AB', set([0, 3, 6])),
            ('ABC', set([0, 6])) ]
        self.assertEqual(found, expected)

    def test6(self):
        ix = SubsequenceIndex('ABACAB')
        found = list( ix.find('AB') )
        expected = [
            ('A', set([0, 2, 4])),
            ('AB', set([0, 4])) ]
        #print('\nfound {}\nexpec {}\n'.format(found, expected))
        #print('ix.root = {}'.format(ix.root))
        self.assertEqual(found, expected)

    def test7(self):
        ix = SubsequenceIndex('X')
        found = list( ix.find('X') )
        expected = [
            ('X', set([0])) ]
        self.assertEqual(found, expected)

    def test8(self):
        ix = SubsequenceIndex('')
        found = list( ix.find('') )
        expected = []
        self.assertEqual(found, expected)

    def test9(self):
        ix = SubsequenceIndex('ABC')
        found = list( ix.find('') )
        expected = []
        self.assertEqual(found, expected)

    def test10(self):
        ix = SubsequenceIndex('')
        found = list( ix.find('ABC') )
        expected = []
        self.assertEqual(found, expected)

    def test11(self):
        ix = SubsequenceIndex('ABCxxxABCDEFxxxABCyyyABCDEFG')
        found = list( ix.find('ABCDEFG') )
        expected = [
            ('ABC', set([0,6,15,21])),
            ('ABCDEF', set([6,21])),
            ('ABCDEFG', set([21]))
        ]
        self.assertEqual(found, expected)

    def test12(self):
        ix = SubsequenceIndex('zzzzzABCxxxABCDEFxxxABCyyyABCDEFG')
        found = list( ix.find('ABCDEFG') )
        expected = [
            ('ABC', set([5,11,20,26])),
            ('ABCDEF', set([11,26])),
            ('ABCDEFG', set([26]))
        ]
        self.assertEqual(found, expected)

    def test13(self):
        ix = SubsequenceIndex('DE')
        found = list( ix.find('ED') )
        expected = [ ('E', set([1])) ]
        self.assertEqual(found, expected)

from dnaPalindrome import dnaPalindromes
        
class testPalindromsElementary(unittest.TestCase):
    def testZero(self):
        found = list(dnaPalindromes(''))
        expected = []
        self.assertEqual(found, expected)

    # def testOneChar(self):
        # found = list(dnaPalindromes('T'))
        # expected = []
        # self.assertEqual(found, expected)

    def testTwoCharPalindrome(self):
        found = list(dnaPalindromes('AT'))
        expected = [('A', set([0])), ('T', set([1]))]
        self.assertEqual(found, expected)

# class testPalindromsShort(unittest.TestCase):
    # def testAllA(self):
        # found = list(dnaPalindromes('AAAAAA'))
        # expected = []
        # self.assertEqual(found, expected)

    # def testLen2Palindrome(self):
        # found = set([ i for i in dnaPalindromes('ATGGAT') if len(i) > 1])
        # expected = set(['AT', 'TA'])
        # self.assertEqual(found, expected)

if __name__ == '__main__':
    unittest.main()

