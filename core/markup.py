#!/usr/bin/python

class Markup(object):
    """various markup specifications share a basic common syntax
    """
    NEWLINE = '\n' #python way
    INDENT_SPACES = ' '*4

    def strong_emphasis(self, text):
        """bold"""
        return "**%s**" % text + self.NEWLINE

    def emphasis(self, text):
        """italic"""
        return "*%s*" % text + self.NEWLINE

    def transition(self):
        return '-' * 6 + self.NEWLINE

    #Lists: bulleted list,  enumerated list, definition
    def bulleted_list(self, list_, indent=0 , bullet_char='-'):
        """Return a bulleted list text with customized parameters

        Args:
            list_: text in list type
            indent: indent level, default no indentation
            bullet_char: start the line off with a bullet point character
                         either "-", "+" or "*", default '-'
        Returns:
            A reST text for bulleted lists
        """

        text = [self.unaligned_text((bullet_char + ' '), line, indent)
            for line in list_]
        return self.NEWLINE.join(text) + self.NEWLINE

    def unaligned_text(self, head, text, indent):
        lines = text.strip().split(self.NEWLINE)
        indent_spaces = self.INDENT_SPACES * indent

        buf = [indent_spaces + head + lines.pop(0)]

        indent_spaces += ' ' * len(head)
        [buf.append(indent_spaces + line.strip()) for line in lines]

        return self.NEWLINE.join(buf)

if __name__ == '__main__':
    markup = Markup()

    print markup.bulleted_list(list('adaddd'))
