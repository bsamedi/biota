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
        self.assertEquals(i.positionsIncludinChildren(), set([]))

    def testositionsRecursive1(self):
        root = IndexNode.new()
        root.addChild('42', set([2,3,42]))
        i = root.getChild('42')
        self.assertEquals(i.positionsIncludinChildren(), set([2,3,42]))

    def testositionsRecursive2(self):
        root = IndexNode.new()
        root.addChild('42', set([2,3,42]))
        i = root.getChild('42')
        i.addChild('T', set([17, 26]))
        self.assertEquals(
            set( root.positionsIncludinChildren() ),
            set([2,3,42,17,26]))

    def testositionsRecursive3(self):
        root = IndexNode.new()
        root.addChild('42', set([2,3,42]))
        root.addChild('bravo', set([3, 100, 42]))
        i = root.getChild('42')
        i.addChild('T', set([4, 17, 26]))
        found = root.positionsIncludinChildren()
        expected = set([2,3,42, 3,100,42,4, 17, 26])
        self.assertEquals(found, expected)

    def testositionsRecursive_Twice(self):
        root = IndexNode.new()
        root.addChild('A', set([1]))
        root.addChild('B', set([4]))
        self.assertEquals(len(root.positions), 0)
        root.positionsIncludinChildren()
        found = root.positionsIncludinChildren()
        self.assertEquals(len(root.positions), 0)

# class testPalindromsElementary(unittest.TestCase):
    # def testZero(self):
        # found = list(dnaPalindromes(''))
        # expected = []
        # self.assertEqual(found, expected)

    # def testOneChar(self):
        # found = list(dnaPalindromes('T'))
        # expected = []
        # self.assertEqual(found, expected)

    # def testTwoCharPalindrome(self):
        # found = set(dnaPalindromes('AT'))
        # expected = set(['A', 'T'])
        # self.assertEqual(found, expected)

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

