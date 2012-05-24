#!/usr/bin/python

from core.markup import Markup

class MarkDown(Markup):
    """Markdown is a text-to-HTML conversion tool for web writers.
    This implementation does not try to cover all the specifications.
    """
    ATX_SIGN = '#'
    def __init__(self):
        [self.add_headers(level) for level in xrange(1,7)]

    def blockquote(self, text, level=1, empty=True):
        """blockquote
        > level 1
        >
        >> level 2
        >>
        """
        _header = '>' * level
        if empty:
            return "{0} {1}\n{0}\n".format(_header, text)
        else:
            return "{} {}".format(_header, text)

    def add_headers(self, level):
        """dynamically add h1-h6 as they are generic except atx sign"""
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
