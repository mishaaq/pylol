#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__="Michał Żarłok"
__date__ ="$2009-12-20 23:35:57$"

import sys
from interpreter import LOLInterpreter
from parser import parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        if argv[1] == '-t':
            with open(sys.argv[2]) as lolfile:
                print parser.parse(lolfile.read())
        else:
            with open(sys.argv[1]) as lolfile:
                tree = parser.parse(lolfile.read())
                interpret = LOLInterpreter(tree)
                interpret.execute()
    except KeyError:
        print "Usage:"
        print "\tpylol.py [-t] <file>\n"

if __name__ == "__main__":
    sys.exit(main());
