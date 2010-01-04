# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-14 22:25:52$"

import ply.yacc as yacc

from lexer import tokens

precedence = (
    ('right', 'IDENTIFIER'),
)

def p_start(p):
    '''program : HAI EOL statement_list KTHXBYE EOL
               | HAI EOL statement_list KTHXBYE'''
    p[0] = p[3]

def p_statement_list(p):
    '''statement_list : statement_list statement EOL
                      | statement EOL'''
    if len(p) == 4:
        p[1].extend([p[2]])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression'''
    p[0] = ['it', p[1]]

def p_statement_print(p):
    '''statement : VISIBLE expression '!'
                 | VISIBLE expression'''
    if len(p) == 4:
        p[0] = ['print', p[2]]
    else:
        p[0] = ['printline', p[2]]

def p_statement_get(p):
    '''statement : GIMMEH IDENTIFIER'''
    p[0] = ['get', p[2]]

def p_statement_define(p):
    '''statement : I_HAS_A IDENTIFIER ITZ expression
                 | I_HAS_A IDENTIFIER'''
    if len(p) == 5:
        p[0] = ['define', p[2], p[4]]
    else:
        p[0] = ['declare', p[2]]

def p_statement_assign(p):
    '''statement : IDENTIFIER R expression'''
    p[0] = ['assign', p[1], p[3]]

def p_statement_convert(p):
    '''statement : IDENTIFIER IS_NOW_A TYPE'''
    p[0] = ['convert', p[1], p[3]]

def p_statement_if(p):
    '''statement : O_RLY EOL YA_RLY EOL statement_list NO_WAY EOL statement_list OIC
                 | O_RLY EOL YA_RLY EOL statement_list OIC'''
    if len(p) == 10:
        p[0] = ['if', p[5], p[8]]
    else:
        p[0] = ['if', p[5]]

def p_statement_loop(p):
    '''statement : IM_IN_YR IDENTIFIER EOL statement_list IM_OUTTA_YR IDENTIFIER'''
    p[0] = ['loop', p[2], p[4], p[6]]

def p_statement_break(p):
    '''statement : GTFO'''
    p[0] = ['break']

def p_statement_function(p):
    '''statement : HOW_DUZ_I IDENTIFIER argument_list EOL statement_list IF_U_SAY_SO'''
    p[0] = ['function', p[2], p[3], p[5]]

# instrukcja: return
def p_statement_return(p):
    '''statement : FOUND_YR expression'''
    p[0] = ['return', p[2]]

def p_argument_list(p):
    '''argument_list : argument_list AN argument
                     | YR argument'''
    if len(p) == 4:
        p[1].extend([p[3]])
        p[0] = p[1]
    else:
        p[0] = [p[2]]

def p_argument(p):
    '''argument : IDENTIFIER'''
    p[0] = p[1]

# wyrażenie: lista wyrażeń
def p_expression_list(p):
    '''expression_list : expression_list AN expression
                       | expression'''
    if len(p) == 4:
        p[1].extend([p[3]])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

# wyrażenie: wywołanie funkcji
def p_expression_call(p):
    '''expression : IDENTIFIER expression_call_list'''
    p[0] = ['call', p[1], p[2]]

# wyrażenie: lista wyrażeń jako argumentów wywołania funkcji
def p_expression_call_list(p):
    '''expression_call_list : expression_call_list expression
                            | expression'''
    if len(p) == 3:
        p[1].extend([p[2]])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

# wyrażenie: operator
def p_expression_operator(p):
    '''expression : expression_unary_operator
                  | expression_binary_operator
                  | expression_inf_arity_operator'''
    p[0] = p[1]

# wyrażenie: operator jednoargumentowy
def p_expression_unary_operator(p):
    '''expression_unary_operator : NOT expression'''
    p[0] = ['not', p[2]]

# wyrażenie: operator dwuargumentowy
def p_expression_binary_operator(p):
    '''expression_binary_operator : SUM_OF expression AN expression
                                  | DIFF_OF expression AN expression
                                  | PRODUCT_OF expression AN expression
                                  | QUOSHUNT_OF expression AN expression
                                  | MOD_OF expression AN expression
                                  | BIGGR_OF expression AN expression
                                  | SMALLR_OF expression AN expression
                                  | BOTH_OF expression AN expression
                                  | EITHER_OF expression AN expression
                                  | WON_OF expression AN expression
                                  | BOTH_SAEM expression AN expression
                                  | DIFFRINT expression AN expression'''
    p[0] = { 'SUM_OF'       : lambda x, y: ['+', x, y],
             'DIFF_OF'      : lambda x, y: ['-', x, y],
             'PRODUCT_OF'   : lambda x, y: ['*', x, y],
             'QUOSHUNT_OF'  : lambda x, y: ['/', x, y],
             'MOD_OF'       : lambda x, y: ['%', x, y],
             'BIGGR_OF'     : lambda x, y: ['>', x, y],
             'SMALLR_OF'    : lambda x, y: ['<', x, y],
             'BOTH_OF'      : lambda x, y: ['&', x, y],
             'EITHER_OF'    : lambda x, y: ['|', x, y],
             'WON_OF'       : lambda x, y: ['^', x, y],
             'BOTH_SAEM'    : lambda x, y: ['==', x, y],
             'DIFFRINT'     : lambda x, y: ['!=', x, y]
           }[p[1]](p[2], p[4])

# wyrażenie: operator wieloargumentowy
def p_expression_inf_arity(p):
    '''expression_inf_arity_operator : ALL_OF expression_list MKAY
                                     | ANY_OF expression_list MKAY'''
    p[0] = {'ALL_OF' : lambda x: ['all', x],
            'ANY_OF' : lambda x: ['any', x]
           }[p[1]](p[2])

# wyrażenie: rzutowanie zmiennej na typ
def p_expression_cast(p):
    '''expression : MAEK IDENTIFIER A TYPE
                  | MAEK IDENTIFIER TYPE'''
    if len(p) == 6:
        p[0] = ['cast', p[2], p[4]]
    else:
        p[0] = ['cast', p[2], p[3]]

# wyrażenie: argument wyrażenia
def p_expression_variable(p):
    '''expression : string
                  | FLOAT
                  | INTEGER
                  | BOOLEAN
                  | variable'''
    p[0] = p[1]

# argument: tekst
def p_string(p):
    '''string : STRING
              | SMOOSH expression_list MKAY'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ['concat', p[2]]

# argument: zmienna
def p_variable(p):
    '''variable : IDENTIFIER'''
    p[0] = ['value', p[1]]
    

def p_error(p):
    print "Syntax error at token %s in line %d" % (p.value, p.lineno)

parser = yacc.yacc(debug=1)

if __name__ == "__main__":
    import sys
    import logging
    logging.basicConfig(
        level = logging.DEBUG,
        filename = "parselog.txt",
        filemode = "w",
        format = "%(filename)10s:%(lineno)4d:%(message)s"
    )
    if sys.argv[1:]:
        with open(sys.argv[1]) as lolfile:
            log = logging.getLogger()
            result = parser.parse(lolfile.read(), debug=log)
            print result
