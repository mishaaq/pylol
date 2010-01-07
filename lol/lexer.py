# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-14 22:25:21$"

import ply.lex as lex

# tokeny
tokens = (
    'IDENTIFIER',
    'STRING',
    'INTEGER',
    'FLOAT',
    'BOOLEAN',
    'I_HAS_A',
    'ITZ',
    'R',
    'MAEK',
    'A',
    'IS_NOW_A',
    'TYPE',
    'VISIBLE',
    'GIMMEH',
    'SUM_OF',
    'DIFF_OF',
    'PRODUCT_OF',
    'QUOSHUNT_OF',
    'MOD_OF',
    'BIGGR_OF',
    'SMALLR_OF',
    'BOTH_OF',
    'EITHER_OF',
    'WON_OF',
    'NOT',
    'ALL_OF',
    'ANY_OF',
    'SMOOSH',
    'MKAY',
    'BOTH_SAEM',
    'DIFFRINT',
    'O_RLY',
    'YA_RLY',
    'NO_WAY',
    'IM_IN_YR',
    'IM_OUTTA_YR',
    'GTFO',
    'HAI',
    'KTHXBYE',
    'HOW_DUZ_I',
    'YR',
    'AN',
    'FOUND_YR',
    'IF_U_SAY_SO',
    'WTF',
    'OMG',
    'OMGWTF',
    'OIC',
    'EOL',
)

literals = ( '!', )

def t_I_HAS_A(t):
    r'I\s+HAS\s+A\b'
    t.value = 'I_HAS_A'
    return t

def t_COMMENT(t):
    r'BTW\s[^\n]*'
    pass

def t_ITZ(t):
    r'ITZ\b'
    t.value = 'ITZ'
    return t

def t_R(t):
    r'R\b'
    return t

def t_MAEK(t):
    r'MAEK\b'
    return t

def t_A(t):
    r'A\b'
    return t

def t_IS_NOW_A(t):
    r'IS\s+NOW\s+A\b'
    t.value = 'IS_NOW_A'
    return t

def t_TYPE(t):
    r'((?:NUMBA?R)|(?:YARN)|(?:TROOF)|(?:NOOB))\b'
    return t

def t_VISIBLE(t):
    r'VISIBLE\b'
    return t

def t_GIMMEH(t):
    r'GIMMEH\b'
    return t

def t_SUM_OF(t):
    r'SUM\s+OF\b'
    t.value = 'SUM_OF'
    return t

def t_DIFF_OF(t):
    r'DIFF\s+OF\b'
    t.value = 'DIFF_OF'
    return t

def t_PRODUCT_OF(t):
    r'PRODUCT\s+OF\b'
    t.value = 'PRODUCT_OF'
    return t

def t_QUOSHUNT_OF(t):
    r'QUOSHUNT\s+OF\b'
    t.value = 'QUOSHUNT_OF'
    return t

def t_MOD_OF(t):
    r'MOD\s+OF\b'
    t.value = 'MOD_OF'
    return t

def t_BIGGR_OF(t):
    r'BIGGR\s+OF\b'
    t.value = 'BIGGR_OF'
    return t

def t_SMALLR_OF(t):
    r'SMALLR\s+OF\b'
    t.value = 'SMALLR_OF'
    return t

def t_BOTH_OF(t):
    r'BOTH\s+OF\b'
    t.value = 'BOTH_OF'
    return t

def t_EITHER_OF(t):
    r'EITHER\s+OF\b'
    t.value = 'EITHER_OF'
    return t

def t_WON_OF(t):
    r'WON\s+OF\b'
    t.value = 'WON_OF'
    return t

def t_NOT(t):
    r'NOT\b'
    return t

def t_ALL_OF(t):
    r'ALL\s+OF\b'
    t.value = 'ALL_OF'
    return t

def t_ANY_OF(t):
    r'ANY\s+OF\b'
    t.value = 'ANY_OF'
    return t

def t_SMOOSH(t):
    r'SMOOSH\b'
    return t

def t_MKAY(t):
    r'MKAY\b'
    return t

def t_BOTH_SAEM(t):
    r'BOTH\s+SAEM\b'
    t.value = 'BOTH_SAEM'
    return t

def t_DIFFRINT(t):
    r'DIFFRINT\b'
    return t

def t_O_RLY(t):
    r'O\s+RLY\?'
    t.value = 'O_RLY'
    return t

def t_YA_RLY(t):
    r'YA\s+RLY\b'
    t.value = 'YA_RLY'
    return t

def t_NO_WAY(t):
    r'NO\s+WAY\b'
    t.value = 'NO_WAY'
    return t

def t_IM_IN_YR(t):
    r'IM\s+IN\s+YR\b'
    t.value = 'IM_IN_YR'
    return t

def t_IM_OUTTA_YR(t):
    r'IM\s+OUTTA\s+YR\b'
    t.value = 'IM_OUTTA_YR'
    return t

def t_GTFO(t):
    r'GTFO\b'
    return t

def t_HAI(t):
    r'HAI\b'
    return t

def t_KTHXBYE(t):
    r'KTHXBYE\b'
    return t

def t_HOW_DUZ_I(t):
    r'HOW\s+DUZ\s+I\b'
    t.value = 'HOW_DUZ_I'
    return t

def t_YR(t):
    r'YR\b'
    return t

def t_AN(t):
    r'AN\b'
    return t

def t_FOUND_YR(t):
    r'FOUND\s+YR\b'
    t.value = 'FOUND_YR'
    return t

def t_IF_U_SAY_SO(t):
    r'IF\s+U\s+SAY\s+SO\b'
    t.value = 'IF_U_SAY_SO'
    return t

def t_WTF(t):
    r'WTF\?'
    t.value = 'WTF'
    return t

def t_OMG(t):
    r'OMG\b'
    return t

def t_OMGWTF(t):
    r'OMGWTF\b'
    return t

def t_OIC(t):
    r'OIC\b'
    return t



def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*?\b'
    t.type = 'IDENTIFIER'
    return t

def t_INTEGER(t):
    r'-?\d+'
    t.type = 'INTEGER'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'-?\d+\.\d+'
    t.type = 'FLOAT'
    t.value = float(t.value)
    return t

def t_STRING(t):
    #TODO: Żeby przepuszczało cudzysłowy
    r'(\"|\')(?:[^:\"]|::|:\")*(\"|\')'
    t.type = 'STRING'
    t.value = t.value[1:-1].decode("string-escape")
    return t

def t_BOOLEAN(t):
    r'(?:WIN)|(?:FAIL)'
    t.type = 'BOOLEAN'
    return t

def t_MULT(t):
    r'(\.{3}\n)|\u2026'
    pass

def t_EOL(t):
    r',|\n'
    if t.value == '\n':
        t.lexer.lineno += 1
    t.value = 'EOL'
    return t

def t_WS(t):
    r'\s+'
    pass

def t_error(t):
    print "Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno)
    t.lexer.skip(1)


lexer = lex.lex(optimize=1)

if __name__ == "__main__":
    lex.runmain()
