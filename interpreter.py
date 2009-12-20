# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-03 23:16:44$"

import types

class Break(Exception):
    pass

class LOLInterpreter(object):

    def __init__(self, tree):
        self.__tree = tree
        self.__variables = []

    def execute(self):
        self.__variables.append({"IT": None})
        self.__execute_statement_list(self.__tree)
    
    def __execute_statement_list(self, statement_list):
        for statement in statement_list:
            self.__execute_statement(statement)
    
    def __execute_statement(self, statement):
        if not statement:
            return
        elif statement[0] == 'print':
            print self.__evaluate_expression(statement[1]),
        elif statement[0] == 'printline':
            print "%s" % self.__evaluate_expression(statement[1])
        elif statement[0] == 'get':
            self.__set_variable(statement[1], raw_input())
        elif statement[0] == 'declare':
            self.__declare_variable(statement[1])
        elif statement[0] == 'define':
            self.__declare_variable(statement[1])
            self.__set_variable(statement[1], self.__evaluate_expression(statement[2]))
        elif statement[0] == 'assign':
            self.__set_variable(statement[1], self.__evaluate_expression(statement[2]))
        elif statement[0] == 'convert':
            if   statement[2] == 'YARN':
                self.__set_variable(statement[1], str(self.__get_variable(statement[1])))
            elif statement[2] == 'NUMBR':
                self.__set_variable(statement[1], int(self.__get_variable(statement[1])))
            elif statement[2] == 'NUMBAR':
                self.__set_variable(statement[1], float(self.__get_variable(statement[1])))
            elif statement[2] == 'TROOF':
                self.__set_variable(statement[1], boolean(self.__get_variable(statement[1])))
            else:
                raise Exception("Cannot convert identifier: %s to type %s" % (statement[1], statement[2]))
        elif statement[0] == 'if':
            pass
        elif statement[0] == 'loop':
            try:
                while(True):
                    self.__execute_statement_list(statement[4])
            except Break:
                pass
        elif statement[0] == 'break':
            raise Break()
        elif statement[0] == 'function':
            # TODO: function definition
            raise Exception("Function definition not implemented yet!")
    
    def __evaluate_expression(self, expression):
        if type(expression) != types.ListType:
            return expression
        if   expression[0] == 'call':
            # TODO: function call
            raise Exception("Function call not implemented yet!")
        elif expression[0] == 'not':
            return not self.__evaluate_expression([1])
        elif expression[0] == '+':
            return self.__evaluate_expression(expression[1]) + self.__evaluate_expression(expression[2])
        elif expression[0] == '-':
            return self.__evaluate_expression(expression[1]) - self.__evaluate_expression(expression[2])
        elif expression[0] == '*':
            return self.__evaluate_expression(expression[1]) * self.__evaluate_expression(expression[2])
        elif expression[0] == '/':
            return self.__evaluate_expression(expression[1]) / self.__evaluate_expression(expression[2])
        elif expression[0] == '%':
            return self.__evaluate_expression(expression[1]) % self.__evaluate_expression(expression[2])
        elif expression[0] == '>':
            return self.__evaluate_expression(expression[1]) > self.__evaluate_expression(expression[2])
        elif expression[0] == '<':
            return self.__evaluate_expression(expression[1]) < self.__evaluate_expression(expression[2])
        elif expression[0] == '&':
            return self.__evaluate_expression(expression[1]) and self.__evaluate_expression(expression[2])
        elif expression[0] == '|':
            return self.__evaluate_expression(expression[1]) or self.__evaluate_expression(expression[2])
        elif expression[0] == '^':
            return not (self.__evaluate_expression(expression[1]) and self.__evaluate_expression(expression[2]))
        elif expression[0] == '==':
            return self.__evaluate_expression(expression[1]) == self.__evaluate_expression(expression[2])
        elif expression[0] == '!=':
            return self.__evaluate_expression(expression[1]) != self.__evaluate_expression(expression[2])
        elif expression[0] == 'all':
            return all([self.__evaluate_expression(expr) for expr in expression[1]])
        elif expression[0] == 'any':
            return any([self.__evaluate_expression(expr) for expr in expression[1]])
        elif expression[0] == 'cast':
            if   expression[2] == 'YARN':
                return str(expression[1])
            elif expression[2] == 'NUMBR':
                return int(expression[1])
            elif expression[2] == 'NUMBAR':
                return float(expression[1])
            elif expression[2] == 'TROOF':
                return boolean(expression[1])
            else:
                raise Exception("Cannot cast expression: %s to type %s" % (expression[1], expression[2]))
        elif expression[0] == 'concat':
            return ''.join(map(lambda item: self.__evaluate_expression(item), expression[1]))
        elif expression[0] == 'value':
                return self.__get_variable(expression[1])
    
    def __get_variable(self, name):
        try:
            return self.__variables[len(self.__variables)-1][name]
        except KeyError:
            raise Exception("Undeclared identifier: %s" % name)

    def __set_variable(self, name, value):
        if name in self.__variables[len(self.__variables)-1]:
            self.__variables[len(self.__variables)-1][name] = value
        else:
            raise Exception("Undeclared identifier: %s" % name)

    def __declare_variable(self, name):
        if name not in self.__variables[len(self.__variables)-1]:
            self.__variables[len(self.__variables)-1][name] = None
        else:
            raise Exception("Multiple declaration of identifier: %s" % name)

if __name__ == "__main__":
    print "Hello World"
