import unittest
from core.parser import CCTRParser
from core.lexer import CCTRLexer


class TestStringMethods(unittest.TestCase):

    test_cases = [
        {
            'input': 'a-z',
            'output': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z'],
            'exception': False
        },
        {
            'input': 'a-z0-9',
            'output': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                       '4', '5', '6', '7', '8', '9'],
            'exception': False
        },
        {
            'input': 'a-z0-9A-Z',
            'output': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                       '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
                       'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z'],
            'exception': False
        },
        {
            'input': '"[:digit:]"',
            'output': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            'exception': False
        },
        {
            'input': 'A-D"[:digit:]"',
            'output': ['A', 'B', 'C', 'D', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
            'exception': False
        },
        {
            'input': '~',
            'output': [],
            'exception': True
        },
    ]

    def test_parser(self):
        for test_case in self.test_cases:
            if not test_case['exception']:
                self.assertEqual(
                    CCTRParser().parse(CCTRLexer().tokenize(test_case['input'])),
                    test_case['output']
                )
            else:
                with self.assertRaises(RuntimeError):
                    CCTRParser().parse(CCTRLexer().tokenize(test_case['input']))

if __name__ == '__main__':
    unittest.main()