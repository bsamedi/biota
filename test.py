#!/usr/bin/env python
import unittest
import mock
from mock import patch
from mock import Mock

import dnaPalindrome

class testChildOps(unittest.TestCase):
    def testNewIndexNode(self):
        i = dnaPalindrome.IndexNode.new()
        self.assertEqual(i.positions, set())
        self.assertEqual(i.children, {})
        
    #@patch('dnaPalindrome.IndexNode')
    def testChildExists(self):
        i = dnaPalindrome.IndexNode.new()
        self.assertEquals(i.childExists('a'), False)

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

