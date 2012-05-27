#!/usr/bin/python

import re
import string
import time
from os.path import sep, abspath

from core.yamlagent import YamlAgent
from core.listmap import ListMap
from core.rest import ReST
from core.markdown import MarkDown
from core.decorators import SafeRead, SafeWrite

class LoadYamlError(Exception):
    pass

class DumpYamlError(Exception):
    pass

class GlossaryData(ListMap, YamlAgent):
    """aadada"""
    def __init__(self, path=''):
        super(GlossaryData, self).__init__()

        self.path = path
        self.wordpat = re.compile("[0-9a-zA-Z_-]+")
        self.keyset = set(self.keys())
        self.rst = ReST()
        self.md = MarkDown()
        self.key_index = ListMap()

    def load_yaml(self, yamlpath=''):
        """load yaml file"""
        if not yamlpath:
            yamlpath = self.path
        try:
            self.update(self.load(yamlpath))
            self.build_key_index()
        except Exception, e:
            raise LoadYamlError(e)

    def dump_yaml(self, yamlpath=''):
        """dump yaml file"""
        if not yamlpath:
            yamlpath = self.path
        try:
            self.dump(yamlpath, self.data)
        except Exception:
            raise DumpYamlError

    def build_key_index(self):
        alphabeta = list(string.ascii_lowercase)
        for letter in alphabeta:
            for abbr in self.data.keys():
                if abbr[0].lower() == letter:
                    self.key_index[letter] = abbr
        self.key_index.sort()
    @SafeWrite
    def write(self, path, buf):
        print "writing >>>", path.name
        path.write(buf)

    @SafeRead
    def read_template(self, path):
        """read the file"""
        return string.Template(path.read())

    def build_markup(self, markup='md', output="/home/byron/code/glossary/output"):
        """docstring for build_md"""
        if markup not in ('rst', 'md'):
            return

        _method = getattr(self, "build_{}".format(markup))
        _output = abspath(
                sep.join((output, 'glossary.{}'.format(markup))))

        self.write(_output, _method())

    def capitalize(self, texts):
        """docstring for capitalize"""
        _capitalized = []
        for text in texts:
            _text = []
            #for word in re.findall(self.wordpat, text):
            for word in text.split():
                _text.append(word[0].upper() + word[1:])
            _capitalized.append(' '.join(_text))
        return _capitalized

    def build_md(self, template='/home/byron/code/glossary/templates/glossary.md'):
        _markdown = []
        _template = self.read_template(template)

        for letter, abbrs in self.key_index.iteritems():
            _markdown.append(self.md.h2(letter.upper()))

            for abbr in abbrs:
                _block = self.md.blockquote(
                    self.capitalize(self.data[abbr]))
                _markdown.append(self.md.strong_emphasis(abbr.upper()))
                _markdown.append(_block)

            _markdown.append(self.md.transition())

        _content = '\n'.join(_markdown)

        return _template.substitute(
            {'time': time.asctime(),
             'content': _content})

if __name__ == '__main__':
    glossary = GlossaryData("/home/byron/code/glossary/data/glossary.yml")
    glossary.load_yaml()
    glossary.build_markup()
