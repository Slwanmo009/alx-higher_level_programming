#!/usr/bin/python3
'''Module for  lookup method'''



def lookup(obj):
    '''looks up object attributes and methods.
    Args:
       obj (object): the object to lisst.
    Return:
         list: the list of attributes
    '''
    return dir(obj)
