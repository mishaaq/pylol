# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-14 22:25:21$"

import ply.lex as lex

# tokeny
tokens = (
    'IDENTIFIER',
    'INTEGER',
    'FLOAT',
    'STRING',
    'OPERATOR',
    'RESERVED',
    'COMA',
    'PERIODS'
)

def t_DECLARE(t):
    r'I\s+HAS\s+A\b'
    t.type = 'RESERVED'
    t.value = 'DECLARE'
    return t

def t_COMMENT(t):
    r'BTW\s[^\n]*'
    pass

def t_PRE(t):
    r'ITZ\b'
    t.type = 'OPERATOR'
    t.value = 'PRE'
    return t

def t_ASSIGNMENT(t):
    r'R\b'
    t.type = 'OPERATOR'
    t.value = 'ASSIGN'
    return t

def t_CAST(t):
    r'MAEK\b'
    t.type = 'RESERVED'
    t.value = 'CAST'
    return t

def t_A(t):
    r'A\b'
    t.type = 'RESERVED'
    return t

def t_CONVERT(t):
    r'IS\s+NOW\s+A\b'
    t.type = 'RESERVED'
    t.value = 'CONVERT'
    return t

def t_TYPE(t):
    r'((?:NUMBA?R)|(?:YARN)|(?:TROOF)|(?:NOOB))\b'
    return t

def t_PRINT(t):
    r'VISIBLE\b'
    t.type = 'RESERVED'
    return t

def t_CRSUPPRESS(t):
    r'!\b'
    t.type = 'RESERVED'
    return t

def t_GET(t):
    r'GIMMEH\b'
    t.type = 'RESERVED'
    return t

def t_SUM(t):
    r'SUM\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'SUM'
    return t

def t_DIFF(t):
    r'DIFF\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'DIFF'
    return t

def t_PROD(t):
    r'PRODUCT\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'PROD'
    return t

def t_DIV(t):
    r'QUOSHUNT\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'DIV'
    return t

def t_MOD(t):
    r'MOD\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'MOD'
    return t

def t_GT(t):
    r'BIGGR\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'GT'
    return t

def t_LT(t):
    r'SMALLR\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'LT'
    return t

def t_AND(t):
    r'BOTH\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'AND'
    return t

def t_OR(t):
    r'EITHER\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'OR'
    return t

def t_XOR(t):
    r'WON\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'XOR'
    return t

def t_NOT(t):
    r'NOT\b'
    t.type = 'OPERATOR'
    return t

def t_ALL(t):
    r'ALL\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'ALL'
    return t

def t_ANY(t):
    r'ANY\s+OF\b'
    t.type = 'OPERATOR'
    t.value = 'ANY'
    return t

def t_ARGEND(t):
    r'MKAY\b'
    t.type = 'RESERVED'
    t.value = 'ARGEND'
    return t

def t_EQ(t):
    r'BOTH\s+SAEM\b'
    t.type = 'OPERATOR'
    t.value = 'EQUALS'
    return t

def t_NEQ(t):
    r'DIFFRINT\b'
    t.type = 'OPERATOR'
    t.value = 'NOTEQUALS'
    return t

def t_IF(t):
    r'O\s+RLY\?\b'
    t.type = 'RESERVED'
    t.value = 'IF'
    return t

def t_TRUE(t):
    r'YA\s+RLY\b'
    t.type = 'RESERVED'
    t.value = 'TRUE'
    return t

def t_FALSE(t):
    r'NO\s+WAY\b'
    t.type = 'RESERVED'
    t.value = 'FALSE'
    return t

def t_LOOP(t):
    r'IM\s+IN\s+YR\b'
    t.type = 'RESERVED'
    t.value = 'LOOP'
    return t

def t_ENDLOOP(t):
    r'IM\s+OUTTA\s+YR\b'
    t.type = 'RESERVED'
    t.value = 'ENDLOOP'
    return t

def t_BREAK(t):
    r'GTFO\b'
    t.type = 'RESERVED'
    t.value = 'BREAK'
    return t

def t_FINISH(t):
    r'KTHXBYE\b'
    t.type = 'RESERVED'
    t.value = 'FINISH'
    return t

def t_FUNCTION(t):
    r'HOW\s+DUZ\s+I\b'
    t.type = 'RESERVED'
    t.value = 'FUNCTION'
    return t

def t_ARGUMENT(t):
    r'YR\b'
    t.type = 'RESERVED'
    t.value = 'ARGUMENT'
    return t

def t_COMA(t):
    r'AN\b'
    t.type = 'RESERVED'
    t.value = ','
    return t

def t_RETURN(t):
    r'FOUND\s+YR\b'
    t.type = 'RESERVED'
    t.value = 'RETURN'
    return t

def t_ENDFUNCTION(t):
    r'IF\s+U\s+SAY\s+SO\b'
    t.type = 'RESERVED'
    t.value = 'ENDFUNCTION'
    return t

def t_SWITCH(t):
    r'WTF\?\b'
    t.type = 'RESERVED'
    t.value = 'SWITCH'
    return t

def t_CASE(t):
    r'OMG\b'
    t.type = 'RESERVED'
    t.value = 'CASE'
    return t

def t_DEFAUTLT(t):
    r'OMGWTF\b'
    t.type = 'RESERVED'
    t.value = 'DEFAULT'
    return t

def t_END(t):
    r'OIC\b'
    t.type = 'RESERVED'
    t.value = 'END'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*?\b'
    t.type = 'IDENTIFIER'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'("|\')[^\'"]*(\'|")'
    t.type = 'STRING'
    t.value = t.value[1:-1].decode("string-escape")
    return t

def t_WS(t):
    r'\s+'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex(debug=1)

if __name__ == "__main__":
    lex.runmain()
