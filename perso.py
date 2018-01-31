import argparse
import os.path
from jinja2 import Environment, PackageLoader, select_autoescape

import docutils
from docutils import core, nodes
from docutils.writers.html5_polyglot import Writer, HTMLTranslator
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.directives.admonitions import Admonition, BaseAdmonition

env = Environment(
    loader=PackageLoader('perso', 'template'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
)

# TODO: This is BAD
class customsection(nodes.General, nodes.Element): pass

class DefinitionDirective(Admonition):
    node_class = nodes.admonition

class FragmentWriter(Writer):
    #def get_transforms(self):
    #    return docutils.writers.Writer.get_transforms(self)

    def assemble_parts(self):
        Writer.assemble_parts(self)
        self.parts['meta'] = self.visitor.metadata

class HTMLFragmentTranslator(HTMLTranslator):
    def __init__(self, document):
        HTMLTranslator.__init__(self, document)
        self.head_prefix = ['', '', '', '']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []

        self.metadata = {}

    def astext(self):
        return ''.join(self.body)

    # we essentially want to make meta values accessible to the document
    def visit_meta(self, node):
        if 'name' in node:
            self.metadata[node['name']] = node['content']

    def depart_meta(self, node):
        pass

    def visit_customsection(self, node):
        self.body.append(self.starttag(node, 'section', ''))
        self.body.append('<h2>' + node.title + '</h2>')

    def depart_customsection(self, node):
        self.body.append('</section>')

class SectionDirective(Directive):

    required_arguments = 1
    final_argument_whitespace = True
    option_spec = {'icon': directives.unchanged}
    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = customsection(text)
        node.title = self.arguments[0]
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class TimelineDirective(Directive):

    has_content = True

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.note()
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

def main():
    """ Entry point for the `perso` static site builder. """
    parser = argparse.ArgumentParser(
            description="Build lescot's personal site.")

    args = parser.parse_args()

    # directives.register_directive('section', SectionDirective)
    # directives.register_directive('timeline', TimelineDirective)
    directives.register_directive('definition', DefinitionDirective)

    writer = FragmentWriter()
    writer.translator_class = HTMLFragmentTranslator

    with open('content/notes/CS/2018-01-30.rst') as source:
        content = core.publish_parts(source = source.read(), writer = writer)
        # parser = Parser()
        # parser.parse(source.read(), document)

    template = env.get_template('index.html')
    output = template.render(content = content['fragment'], **content['meta'])


    with open('build/lecture.html', 'w') as target:
        target.write(output)

