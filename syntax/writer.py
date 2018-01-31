from docutils import nodes
from docutils.writers import Writer
import docutils.writers.html5_polyglot as html5

class HTML5Writer(html5.Writer):
    def __init__(self):
        super().__init__()
        self.parts = {}
        self.translator_class = HTML5Translator

    def assemble_parts(self):
        super().assemble_parts()
        self.parts['meta'] = self.visitor.metadata

class HTML5Translator(html5.HTMLTranslator):
    def __init__(self, document):
        super().__init__(document)
        self.head_prefix = ['', '', '', '']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []

        self.metadata = {}

    def astext(self):
        return ''.join(self.body)

    def visit_annotation(self, node):
        self.body.append(self.starttag(node, 'div'))
        print(node)

    def depart_annotation(self, node):
        self.body.append('</div>')

    def visit_icon(self, node):
        self.body.append('<i class="'+ ' '.join(node['classes']) +'"></i>')

    def depart_icon(self, node):
        pass

    # we essentially want to make meta values accessible to the document
    def visit_meta(self, node):
        if 'name' in node:
            self.metadata[node['name']] = node['content']

    def depart_meta(self, node): pass
