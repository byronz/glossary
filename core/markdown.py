#!/usr/bin/python
import types
from core.markup import Markup

class MarkDown(Markup):
    """Markdown is a text-to-HTML conversion tool for web writers.
    This implementation does not try to cover all the specifications.
    """
    ATX_SIGN = '#'
    def __init__(self):
        [self.add_headers(level) for level in xrange(1,7)]

    def blockquote(self, texts, level=1, sign=''):
        """blockquote
        > level 1
        >
        >> level 2
        >>
        text might be a list of string or simply a string
        """
        _header = '>' * level
        _quote = []
        if isinstance(texts, types.StringType):
            texts = (texts,)

        for text in texts:
            _quote.append("{}{} {}\n".format(_header, sign, text))

        _delimiter = _header + self.NEWLINE
        return _delimiter.join(_quote)

    def add_headers(self, level):
        """dynamically add h1-h6

        the outputs are generic except atx sign numbers
        """
        def _header(title):
            return "{} {}\n".format(self.ATX_SIGN * level, title)
        _name = 'h{}'.format(level)
        _header.__name__ = _name
        setattr(self, _name, _header)

if __name__ == '__main__':
    md = MarkDown()
    for level in xrange(1,7):
        _header = getattr(md, "h{}".format(level))
        print _header("level: {}".format(level))

    print dir(md)
    text = ['Application Requirement Specification',
            'Application Research Studies']
    print md.blockquote(text, 2, '*')
