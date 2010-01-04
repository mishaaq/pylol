# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-03 23:16:44$"

import types

class Break(Exception):
    pass

class Return(Exception):
    pass

class LOLInterpreter(object):

    def __init__(self, tree):
        self.__tree = tree
        self.__variables = []

    def execute_program(self):
        self.__variables.append({'IT': None})
        self.__execute_statement_list(self.__tree)

    def __execute_statement_list(self, statement_list):
        if statement_list:
            try:
                for statement in statement_list:
                    self.__execute_statement(statement)
            except Break:
                raise Break
            except Return:
                raise Return
            except Exception as e:
                print e
    
    def __execute_statement(self, statement):
        if not statement:
            return
        elif statement[0] == 'print':
            print self.__print_string(self.__evaluate_expression(statement[1])),
        elif statement[0] == 'printline':
            print self.__print_string(self.__evaluate_expression(statement[1]))
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
            if self.__get_variable('IT') == True:
                self.__execute_statement_list(statement[1])
            elif len(statement) == 3:
                self.__execute_statement_list(statement[2])
        elif statement[0] == 'loop':
            try:
                while(True):
                    self.__execute_statement_list(statement[2])
            except Break:
                pass
        elif statement[0] == 'switch':
            it = self.__get_variable('IT')
            try:
                default = True
                for case in statement[1]:
                    if it == case[0] or not default:
                        self.__execute_statement_list(case[1])
                        default = False
                if default == True:
                    self.__execute_statement_list(statement[2])
            except Break:
                pass
        elif statement[0] == 'break':
            raise Break()
        elif statement[0] == 'function':
            self.__declare_variable(statement[1])
            self.__set_variable(statement[1], [statement[2], statement[3]])
        elif statement[0] == 'return':
            self.__set_variable('IT', self.__evaluate_expression(statement[1]))
            raise Return()
        elif statement[0] == 'it':
            self.__set_variable('IT', self.__evaluate_expression(statement[1]))
    
    def __evaluate_expression(self, expression):
        try:
            if type(expression) != types.ListType:
                return expression
            if expression[0] == 'call':
                function = self.__get_variable(expression[1])
                values = [self.__evaluate_expression(call_argument) for call_argument in expression[2]]
                try:
                    self.__variables.append({'IT' : None})
                    for argument, value in zip(function[0], values):
                        self.__declare_variable(argument)
                        self.__set_variable(argument, value)
                    self.__execute_statement_list(function[1])
                except Break:
                    ret = None
                except Return:
                    ret = self.__get_variable('IT')
                finally:
                    self.__variables.pop()
                return ret
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
                return ''.join(map(lambda item: str(self.__evaluate_expression(item)), expression[1]))
            elif expression[0] == 'value':
                    return self.__get_variable(expression[1])
        except TypeError:
            raise Exception("Unsupported operand type(s) for %s: %s" % (expression[0], ' and '.join(map(lambda x: str(type(x)), map(lambda y: self.__evaluate_expression(y), expression[1:])))))
    
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

    def __print_string(self, string):
        string = string.replace(':)', '\n').replace(':>', '\t').replace(':o', '\g').replace(':"', '"').replace('::', ':')
        return string

if __name__ == "__main__":
    print "Hello World"
