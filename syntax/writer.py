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
        self.math_output = 'mathjax'

    def astext(self):
        return ''.join(self.body)

    def visit_section(self, node):
        self.section_level += 1
        self.body.append(self.starttag(node, 'section'))

    def depart_section(self, node):
        self.section_level -= 1
        self.body.append('</section>')

    def visit_annotation(self, node):
        self.body.append(self.starttag(node, 'div'))

    def depart_annotation(self, node):
        self.body.append('</div>')

    def visit_statement(self, node):
        self.body.append(self.starttag(node, 'figure'))
        self.body.append('<figcaption>')
        self.body.append(node['type'])

        if 'title' in node:
            self.body.append(': ' + node['title'])

        self.body.append('</figcaption>')
        self.body.append(self.starttag({}, 'div'))

    def depart_statement(self, node):
        self.body.append('</div>')
        self.body.append('</figure>')

    def visit_icon(self, node):
        self.body.append('<i class="'+ ' '.join(node['classes']) +'"></i>')

    def depart_icon(self, node):
        pass

    # we essentially want to make meta values accessible to the document
    def visit_meta(self, node):
        if 'name' in node:
            self.metadata[node['name']] = node['content']

    def depart_meta(self, node): pass
