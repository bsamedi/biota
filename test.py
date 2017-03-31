#!/usr/bin/env python
import unittest
import mock
from mock import patch
from mock import Mock

from dnaPalindrome import dnaPalindromes
from dnaPalindrome import SubsequenceIndex

class testChildOps(unittest.TestCase):
    @patch('dnaPalindrome.SubsequenceIndex')
    def testgetChild(self, mock_index):
        s = mock_index()
        s.getChild = Mock(return_value=3)
        self.assertEqual(s.getChild(), 4)

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

