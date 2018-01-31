import docutils
from docutils.parsers.rst import Directive, nodes
from docutils.parsers.rst import states, directives
from docutils.parsers.rst.roles import set_classes

from syntax import nodes

""" Generic directive for annotations related to the main content. """

class Annotation(Directive):
    option_spec = {'class': directives.class_option}
    has_content = True

    def run(self):
        set_classes(self.options)
        self.assert_has_content()

        classes = ['annotation', docutils.nodes.make_id(self.__class__.__name__)]

        if 'classes' in self.options:
            classes.extend(self.options['classes'])

        text = '\n'.join(self.content)
        node = nodes.annotation(text, classes=classes, **self.options)
        # self.add_name(node)

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


class Remark(Annotation): pass
class Note(Annotation): pass
class Attention(Annotation): pass


directives.register_directive('note', Note)
directives.register_directive('remark', Remark)
directives.register_directive('warning', Attention)
