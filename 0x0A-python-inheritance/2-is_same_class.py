#!/usr/bin/python3
'''Module for the _same_ class methods'''


def is_same_class(obj, a_class):
    '''Determains if an object is exactly an instance of a class'''
    return type(obj) == a_class
