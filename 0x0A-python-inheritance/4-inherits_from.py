#!/usr/bin/python3
'''Module for inherited_from method,'''


def inherits_from(obj, a_class):
    '''Detarmain if an object is a true subclass of class'''
    return isinstance (obj, a_class) and type (obj) != a_class
