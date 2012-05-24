#!/usr/bin/python

import types

from core.markup import Markup

class ReST(Markup):
    """docstring for ReST"""

    def h1(self, title):
        """
        =====
        Title
        =====

        """
        return self._dual_adornment(title, '=')

    def h2(self, title):
        return self._dual_adornment(title, '-')

    def h3(self, title):
        return self._single_adornment(title, '=')

    def h4(self, title):
        return self._single_adornment(title, '-')

    def _single_adornment(self, title, adornment):
        return "%s\n%s\n" % (title, adornment * len(title))

    def _dual_adornment(self, title, adornment):
        adornments = adornment * len(title)
        return "%s\n%s\n%s\n" % (adornments, title, adornments)

    def enumerated_list(self, list_, indent=0):
        text = [self.unaligned_text('#. ', line, indent)
            for line in list_]

        return self.NEWLINE.join(text) + self.NEWLINE

    def definition(self, term, definition, indent=0):
        """Return a definition with customized parameters

        **term**
          definition text

        Args:
            term: the term to be defined
            definition: the definition
            indent: indent level, default no indentation

        Returns:
            A ReST text for definition
        """

        indent_space = self.INDENT_SPACES * indent
        buf = [indent_space + self.strong_emphasis(term)]
        indent_space += self.INDENT_SPACES
        buf.append(self.indent_text(definition, indent+1))

        return self.NEWLINE.join(buf)

    def indent_text(self, text, indent=0):
        indent_spaces = self.INDENT_SPACES * indent
        lines = text.split(self.NEWLINE)
        buf = [indent_spaces + line for line in lines]
        return self.NEWLINE.join(buf)

    #Directives-Tables: list table, csv Tables

    def directive(self, type_, content, arguments='', options=[], indent=0):
        """directive marker = explicit markup + type + two colons
        arguments (optional or required), options and block
        +-------+-------------------------------+
        | ".. " | directive type "::" directive |
        +-------+ block                         |
                |                               |
                +-------------------------------+
        .. type:: arguments
            :options:

            content
        """
        indent_spaces = self.INDENT_SPACES * indent
        marker = ".. %s:: " % type_

        lines = [indent_spaces + marker + arguments]

        if options:
            lines.append(self._options(options, indent))

        lines.append(self.NEWLINE)
        lines.append(content + self.NEWLINE)

        return self.NEWLINE.join(lines)

    def _options(self, options, indent):
        buf = []
        for option in options:
            name, value = option
            buf.append(self.field(name, value, indent+1))
        return self.NEWLINE.join(buf)

    def nested_lists(self, nested_lists, indent=0):
        indent_spaces = self.INDENT_SPACES * indent
        buf = []
        for lists in nested_lists:
            head = indent_spaces + '* - '
            for entity in lists:
                #entity might be string or list
                if isinstance(entity, types.ListType):
                    buf.append(self._unaligned_list(head, entity, 0, 'bulleted'))
                    head = indent_spaces + '  - '
                else:
                    buf.append(head + entity)
                    head = indent_spaces + '  - '
        return self.NEWLINE.join(buf)

    #Fields

    def field(self, name, body, indent=0, list_type='bulleted'):
        """Return a field reST text with customized parameters
        The field body can be a list or a multi-lines string

        Args:
            name: the field name
            body: string or list
            list_type: bulleted or enumerated list, by default bulleted
            indent: indent level, by default no indentation
        """
        head = ':%s: ' % name
        if isinstance(body, types.ListType):
            return self._unaligned_list(head, body, indent, list_type)
        elif self.is_multilines(body):
            return self.unaligned_text(head, body, indent)
        else:
            return self.INDENT_SPACES * indent + head + body

    def _unaligned_list(self, head, list_, indent, list_type):

        text = getattr(self, list_type+'_list')(list_)
        return self.unaligned_text(head, text, indent)

    #Tables, simple table
    #support the simple way
    def is_multilines(self, text):
        return len(text.strip().split(self.NEWLINE)) > 1

if __name__ == '__main__':

    obj = ReST()
    print obj.bulleted_list(list('abcbd'), 1)
    print obj.enumerated_list(list('abcdef'), 1)
    print obj.emphasis('aaa')
    print obj.strong_emphasis('aaa')
    print obj.h1('adadad')
    print obj.h4('adaa')

    text = '1. Call secRsaGenerateKey() twice with xKeySize=256, xE=3/17. The\n   reutrn shall be SEC_NO_ERROR. Save two set of outputs as PT64A \n   (n, p, q, dP, dQ, QInv) for e=3 and PT64B for e=17.\n2. Note the two set of RSA key pairs are generated for Alice and Bob.\n    - Alice: PUBa = (3, PT64A.n), PVTa = PT64A[1:5]\n    - Bob: PUBb = (17, PT64B.n), PVTb = PT64B[1:5]\n3. Use a 256-bytes dummy data block X256 as input message. Do the\n   following RSA operation with xPadding=SEC_RSA_NO_PADDING:\n    - secRsaPublicEncrypt(X256, PUBb, X256_PUBb)\n    - secRsaPrivateEncrypt(X256_PUBb, PVTa, X256_PUBb_PVTa)\n    - secRsaPublicDecrypt(X256_PUBb_PVTa, PUBa, D1)\n    - secRsaPrivateDecrypt(D1, PVTb, D2)\n   Check that D1 == X256_PUBb and D2 == X256.   \n'

    print obj.definition('Description', text)

    criteria = ['All returns shall be SEC_NO_ERROR\n', 'Step 3, D1==X256_PUBb and D2==X256\n']
    print obj.definition('Criteria', obj.bulleted_list(criteria))
    print obj.is_multilines('adadaa\n')
    print obj.field('step', text, 1)
    print obj.field('authors', ['byron','sam'])
