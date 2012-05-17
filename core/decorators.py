#!/usr/bin/python

class SafeRead(object):
    """decorator to read file with context manager"""
    def __init__(self, func):
        self.func = func
    def __call__(self, path):
        with open(path, 'rt') as _fp:
            return self.func(self, _fp)

class SafeWrite(object):
    """docstring for SafeWrite"""
    def __init__(self, func):
        self.func = func
    def __call__(self, path, data):
        """docstring for __call__"""
        with open(path, 'wt') as _fp:
            self.func(self, _fp, data)



