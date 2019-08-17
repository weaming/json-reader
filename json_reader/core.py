import re
import inspect

_newline_pattern = re.compile(r'\r\n|\r')


class Lexer:
    def __call__(self, text):
        tokens = []
        return tokens


class Grammar:
    pass


class Renderer:
    pass


def preprocessing(text, tab=4):
    text = _newline_pattern.sub('\n', text)
    text = text.expandtabs(tab)
    text = text.replace('\u2424', '\n')
    pattern = re.compile(r'^ +$', re.M)
    return pattern.sub('', text)


class JSON:
    def __init__(self, renderer=None, lexer=None, **kwargs):
        if not renderer:
            renderer = Renderer(**kwargs)
        else:
            kwargs.update(renderer.options)

        if lexer and inspect.isclass(lexer):
            lexer = lexer(**kwargs)

        self.renderer = renderer
        self.lexer = lexer or Lexer()

        self.tokens = []
        self.token = None

    def read(self, text):
        out = self.output(preprocessing(text))
        return out

    def tok(self):
        t = self.token['type']

        if t.endswith('_start'):
            t = t[:-6]

        return getattr(self, 'output_%s' % t)()

    def output(self, text):
        self.tokens = self.lexer(text)
        out = ""
        while self.pop():
            out += self.tok()
        return out

    def pop(self):
        if not self.tokens:
            return None
        self.token = self.tokens.pop()
        return self.token
