import docutils
from docutils.parsers.rst import Directive, nodes
from docutils.parsers.rst import states, directives
from docutils.parsers.rst.roles import set_classes

from syntax import nodes

class Statement(Directive):
    option_spec = {'class': directives.class_option}
    has_content = True
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self):
        set_classes(self.options)
        self.assert_has_content()

        classes = ['statement', docutils.nodes.make_id(self.__class__.__name__)]

        if 'classes' in self.options:
            classes.extend(self.options['classes'])

        text = '\n'.join(self.content)
        node = nodes.statement(text, classes=classes, **self.options)
        node['type'] = self.__class__.__name__

        if len(self.arguments) == 1:
            node['title'] = self.arguments[0]

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]

class Lemma(Statement): pass
class Theorem(Statement): pass
class Prop(Statement): pass
class Proof(Statement): pass
class Example(Statement): pass
class Definition(Statement): pass

directives.register_directive('lemma', Lemma)
directives.register_directive('theorem', Theorem)
directives.register_directive('prop', Prop)
directives.register_directive('proof', Proof)
directives.register_directive('example', Example)
directives.register_directive('definition', Definition)
