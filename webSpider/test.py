#!/usr/bin/python

############################################################################
import sys
import os
#import trace

sys.path.insert(0,os.path.abspath(os.path.pardir))
import trace

__author__ = "ewentzh"
__date__   = "$2012-7-1$"



def test__trace():
    trace.error("Here is the Error!!!")


def test__getPage():
    print "getPage\n"



if __name__ == "__main__":
#   test__getPage()
    test__trace()


