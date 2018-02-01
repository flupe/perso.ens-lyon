from docutils.parsers.rst import roles
from docutils.parsers.rst import directives

from syntax import nodes

# FontAwesome custom role
def fa_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    classes = ['fas', 'fa-' + text]
    roles.set_classes(options)

    if 'classes' in options:
        classes.extend(options['classes'])

    node = nodes.icon(text, classes=classes)

    return [node], []

fa_role.options = {'class': directives.class_option}

roles.register_canonical_role('fa', fa_role)

