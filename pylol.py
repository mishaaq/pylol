#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-20 23:35:57$"

import sys
from lol.interpreter import LOLInterpreter
from lol.parser import parser

def number_generator():
    i = 1
    while(True):
        yield i
        i = i + 1

def lolconsole():
    print 'PyLOL console v0.1:'
    program = ''
    generator = number_generator()
    while(True):
        try:
            program += raw_input('%d >> ' % generator.next()) + '\n'
        except EOFError:
            break
    print '\n'
    return program

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        if argv[1] == '-t':
            if argv[2] != 'stdin':
                with open(argv[2]) as lolfile:
                    print parser.parse(lolfile.read())
            else:
                program = lolconsole()
                if program:
                    print parser.parse(program)
        else:
            tree = None
            if argv[1] != 'stdin':
                with open(argv[1]) as lolfile:
                    tree = parser.parse(lolfile.read())
            else:
                program = lolconsole()
                if program:
                    tree = parser.parse(program)
            if tree:
                interpret = LOLInterpreter(tree)
                interpret.execute_program()
    except KeyError:
        print "Usage:"
        print "\tpylol.py [-t] (<file>|stdin)\n"
    except IOError:
        print "No such file or directory: %s" % (argv[2] if len(argv) == 3 else argv[1])

if __name__ == "__main__":
    sys.exit(main());
