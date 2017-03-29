import unittest

from dnaPalindrome import dnaPalindromes

class testSimplePalindroms(unittest.TestCase):
    def testZero(self):
        found = list(dnaPalindromes(''))
        expected = []
        self.assertEqual(found, expected)

    def testOneChar(self):
        found = list(dnaPalindromes('T'))
        expected = []
        self.assertEqual(found, expected)

    def testTwoCharPalindrome(self):
        found = set(dnaPalindromes('AT'))
        expected = set(['A', 'T'])
        self.assertEqual(found, expected)


if __name__ == '__main__':
    unittest.main()

