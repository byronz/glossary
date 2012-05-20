#!/usr/bin/python

from UserDict import UserDict
class ListMap(UserDict):
    """Customized dictionary to set item in a list"""
    def __init__(self, **args):
        UserDict.__init__(self, **args)

    def __setitem__(self, key, item):
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(item)

    def update(self, data):
        """update here only accept a dictionary"""
        [self._merge(k,v) for k,v in data.iteritems()]

    def _merge(self, key, value):
        """merge the given key-value with current data
        1. key already in the dictionary
        2. new key
        """
        if key in self.data:
            if iterable(value):
                self.data[key].extend(value)
            else:
                self.data[key].append(value)
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
