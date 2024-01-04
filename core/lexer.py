from sly import Lexer


class CCTRLexer(Lexer):

    tokens =  {
        CHAR, ALNUM, ALPHA, BLANK, CNTRL, DIGIT, LOWER, PRINT, PUNCT, RUNE, SPACE, SPECIAL, UPPER
    }

    literals = { '-', '"', '[', ']', ':' }

    ALNUM = r'alnum'
    ALPHA = r'alpha'
    BLANK = r'blank'
    CNTRL = r'cntrl'
    DIGIT = r'digit'
    LOWER = r'lower'
    PRINT = r'print'
    PUNCT = r'punct'
    RUNE = r'rune'
    SPACE = r'space'
    SPECIAL = r'special'
    UPPER = r'upper'

    CHAR = r'[A-Za-z0-9]{1}'

    @_(r'\n+')
    def newline(self, t: any) -> None:
        self.lineno += t.value.count('\n')

    def error(self, t):
        raise ValueError('Illegal character %r' % t.value[0])
