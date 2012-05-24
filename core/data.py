#!/usr/bin/python

import re
from os.path import sep, abspath

from core.yamlagent import YamlAgent
from core.listmap import ListMap
from core.rest import ReST
from core.decorators import SafeRead, SafeWrite

class LoadYamlError(Exception):
    pass

class GlossaryData(ListMap, YamlAgent):
    """aadada"""
    def __init__(self, path):
        super(GlossaryData, self).__init__()

        self.path = path
        self.wordpat = re.compile("[0-9a-zA-Z_-]+")
        self.keyset = set(self.keys())
        self.rst = ReST()

    def load_yaml(self, yamlpath):
        """load yaml file"""
        if not yamlpath:
            yamlpath = self.path

        try:
            self.update(self.load(yamlpath))
        except Exception:
            raise LoadYamlError

    @SafeWrite
    def write(self, path, buf):
        path.write(buf)

    def build_markup(self, markup='rst', output="./output"):
        """docstring for build_md"""
        if markup not in ('rst', 'md'):
            return

        _method = getattr(self, "build_{}".format(markup))
        _output = abspath(
                sep.join((output, 'glossary.{}'.format(markup))))

        self.write(_output, _method())

    def build_md(self, template='./templates/glossary.md'):
        content = []
        for abbr, descriptions in self.data.iteritems():
            
        _pat_md = re.compile("^(.*?) @")

    def index_descriptions(self, descriptions):
        """
        """
        #['asdada','aa adad @asa']
        buf = []
        for description in descriptions:
            for indexed_word in re.findall(self.wordpat, description):
                if indexed_word in self.keyset:
                    description.
        if word in self.keyset:
            return self.rst.implicit_hyperlink(word)
        else:
            return word

if __name__ == '__main__':
    pass
