#!/usr/bin/python

import yaml

from utils.safefile import *

data = {
    "MAOV": ["Model As Oracle Verification",],
    }

class SafeReadText(object):
    """decorator to read file with context manager"""
    def __init__(self, func):
        self.func = func

    def __call__(self, path):
        with open(path, 'rt') as _fp:
            return self.func(self, _fp)

class SafeWriteText(object):
    """decorator to write file with context manager"""
    def __init__(self, func):
        self.func = func

    def __call__(self, path):
        """docstring for __call__"""
        with open(path, 'wt') as _fp:
            return self.func(self, _fp)

class Data(object):
    """Data class defines the main data structure, includes the major
       methods to manipulate the data including merge and export.

       #Data Structure
            {Term: [Def1, ...],}
    """
    def __init__(self, data_format, path='./data/glossary.yml'):
        self.data_format = data_format

        self.glossary = load_data(path)

    @SafeReadText
    def load_data(self, fp):
        """docstring for load_data"""


    def dump_data(self):
        """docstring for dump_data"""
        pass

    def merge(self, files):
        """merge files, dump the merged glossary data

        """
        [self.merge_file(file_) for file_ in files if is_valid(file_)]


    def compare_datum(self, current, merging):
        """return True if two data set have intersection"""
        return set(current.keys()).intersection(merging.keys())

    def merge_file(self, file_):
        """glossary data is merged with file_

        solve two problems: key conflicts and value update

        Args:
            file_: merging file path

        Returns:
            None
        """
        self.merging_data = getattr(self, 'get_%s' % self.data_format)(file_)

        if self.compare_datum(self.glossary,
