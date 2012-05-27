#!/usr/bin/python

import types
from UserDict import UserDict

class ListMap(UserDict):
    """Customized dictionary to set item in a list"""
    def __init__(self, **args):
        UserDict.__init__(self, **args)

    def __setitem__(self, key, item):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(item)
    def sort(self):
        for k in self.data.keys():
            self.data[k].sort()
    def update(self, data):
        """update here only accepts a dictionary or a nested list/tuple"""
        if isinstance(data, (types.ListType, types.TupleType)):
            [self._merge(*item) for item in data]
        elif isinstance(data, types.DictType):
            [self._merge(k,v) for k,v in data.iteritems()]

        self._update_attributes()

    def _update_attributes(self):
        [setattr(self, k, v) for k,v in self.data.iteritems()]

    def _merge(self, key, value):
        """merge the given key-value with current data
        1. key already in the dictionary
        2. new key
        """
        if key in self.data:
            if isinstance(value, (types.ListType, types.TupleType)):
                self.data[key].extend(value)
            else:
                self.data[key].append(value)
            #eliminate the duplicated description
            self.data[key] = list(set(self.data[key]))
        else:
            self.data[key] = []
            self._merge(key, value)

if __name__ == '__main__':
    td = ListMap()
    td[2]=2
    td[2]=3
    td[3]=121

    td.update()
    print td
    print td.keys()
    print td.values()
