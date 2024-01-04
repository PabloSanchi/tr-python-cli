import unittest
from core.range_base import RangeBase
from core.range_deleter import RangeDeleter
from core.range_squeezer import RangeSqueezer
from core.range_mapper import RangeMapper
from core.lexer import CCTRLexer
from core.parser import CCTRParser

class TestRangeConversors(unittest.TestCase):

    lexer: CCTRLexer = CCTRLexer()
    parser: CCTRParser = CCTRParser()
    test_cases = [
        {
            'class': 'mapper',
            'args': ['A-Z', 'a-z'],
            'input': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'output': 'abcdefghijklmnopqrstuvwxyz',
        },
        {
            'class': 'mapper',
            'args': ['[:upper:]', '[:lower:]'],
            'input': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'output': 'abcdefghijklmnopqrstuvwxyz',
        },
        {
            'class': 'mapper',
            'args': ['A-Z', '[:digit:]'],
            'input': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'output': '01234567899999999999999999',
        },
        {
            'class': 'deleter',
            'args': ['hello'],
            'input': 'hi, how are u doing ?',
            'output': 'i, w ar u ding ?',
        },
        {
            'class': 'squeezer',
            'args': ['AB'],
            'input': 'AABBBBCCCCCDDDDDD',
            'output': 'ABCCCCCDDDDDD',
        }
    ]
    
    def _get_strategy(self, class_name: str, args) -> RangeBase:
        
        if class_name == 'deleter':
            return RangeDeleter(src_range=args[0])
        elif class_name == 'squeezer':
            return RangeSqueezer(src_range=args[0])
        elif class_name == 'mapper':
            if len(args) == 2:
                return RangeMapper(src_range=args[0], to_range=args[1])
            else:
                raise ValueError('Mapper requires two arguments')
        else:
            raise ValueError('Invalid strategy class name')

    
    def test_range_conversor(self):
        for test_case in self.test_cases:
            
            args = [self.parser.parse(self.lexer.tokenize(arg)) for arg in test_case['args']]
            
            strategy: RangeBase = self._get_strategy(
                test_case['class'],
                args
            )
            
            self.assertEqual(strategy.execute(test_case['input']), test_case['output'])
            
if __name__ == '__main__':
    unittest.main()