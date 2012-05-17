#!/usr/bin/python

import yaml
from pprint import pprint
try:
    from yaml import CLoader as Loader
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from core.decorators import SafeRead, SafeWrite

class YamlAgent(object):
    """stand way to load and dump yaml files"""

    @SafeRead
    def load(self, path):
        return yaml.load(path, Loader=Loader)

    @SafeWrite
    def dump(self, path, data):
        """docstring for dump"""
        yaml.dump(
            data, path, Dumper=Dumper, indent=4,
            canonical=False, default_flow_style=False)

if __name__ == '__main__':
    ya = YamlAgent()
    data1 = {'aa': list('asdadad')}
    f = '/tmp/test'
    ya.dump(f, data1)
    data2 = ya.load(f)
    print data1, data2
    print data1 == data2

