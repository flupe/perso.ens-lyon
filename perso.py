import argparse
import os.path
from jinja2 import Environment, PackageLoader, select_autoescape
import docutils
from docutils import core

from syntax.writer import HTML5Writer

import syntax.roles
import syntax.directives.annotations

env = Environment(
    loader=PackageLoader('perso', 'template'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
)

def main():
    """ Entry point for the `perso` static site builder. """
    parser = argparse.ArgumentParser(
            description="Build lescot's personal site.")

    args = parser.parse_args()

    # directives.register_directive('section', SectionDirective)
    # directives.register_directive('timeline', TimelineDirective)
    # directives.register_directive('definition', DefinitionDirective)

    writer = HTML5Writer()

    with open('content/index.rst') as source:
        content = core.publish_parts(source = source.read(), writer = writer)
        # parser = Parser()
        # parser.parse(source.read(), document)

    template = env.get_template('index.html')
    output = template.render(content = content['fragment'], **content['meta'])


    with open('build/index.html', 'w') as target:
        target.write(output)

