from core.lexer import CCTRLexer
from sly import Parser
import os


class CCTRParser(Parser):
    tokens = CCTRLexer.tokens
    
    @_('input token')
    def input(self, p):
        return p.input + p.token
    
    @_('token')
    def input(self, p):
        return p.token
    
    @_('')
    def input(self, p):
        return []
    
    @_('"[" ":" classname ":" "]" ')
    def token(self, p):
        return p.classname
    
    @_('CHAR cont')
    def token(self, p):
        return [p.CHAR] + p.cont
    
    @_('empty "-" CHAR')
    def cont(self, p):
        char_range = [ chr(char) for char in range(ord(p.empty) + 1, ord(p.CHAR)+1)]
        return char_range
     
    @_('')
    def empty(self, p):
        return p[-1]
    
    @_('')
    def cont(self, p):
        return []
    
    @_('ALNUM')
    def classname(self, p):
        return \
            [chr(char) for char in range(ord('A'), ord('Z')+1)] \
            + \
            [chr(char) for char in range(ord('a'), ord('z')+1)] \
            + \
            [chr(char) for char in range(ord('0'), ord('9')+1)]
            
        
    @_('ALPHA')
    def classname(self, p):
        return \
            [chr(char) for char in range(ord('A'), ord('Z')+1)] \
            + \
            [chr(char) for char in range(ord('a'), ord('z')+1)] \
            
    @_('BLANK')
    def classname(self, p):
        return ['', '\t']
    
    @_('CNTRL')
    def classname(self, p):
        return [chr(char) for char in range(0, 31+1)] + [chr(127)]
        
    @_('DIGIT')
    def classname(self, p):
        return [chr(char) for char in range(ord('0'), ord('9')+1)]
        
    @_('LOWER')
    def classname(self, p):
        return [chr(char) for char in range(ord('a'), ord('z')+1)]
        
    @_('PRINT')
    def classname(self, p):
        return [chr(char) for char in range(32, 126+1)]
        
    @_('PUNCT')
    def classname(self, p):
        return \
            [chr(char) for char in range(33, 47+1)] \
            + \
            [chr(char) for char in range(58, 64+1)] \
            + \
            [chr(char) for char in range(91, 96+1)] \
            + \
            [chr(char) for char in range(123, 126+1)]
        
    @_('RUNE')
    def classname(self, p):
        return [ord(char) for char in range(32, 127)]
        
    @_('SPACE')
    def classname(self, p):
        return [chr(9), chr(10), chr(11), chr(12), chr(13), chr(32)]
        
    @_('SPECIAL')
    def classname(self, p):
        return ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']

    @_('UPPER')
    def classname(self, p):
        return [chr(char) for char in range(ord('A'), ord('Z')+1)]
