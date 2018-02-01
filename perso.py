import argparse, os, shutil
from os.path import join, relpath, getmtime, isfile, isdir
import glob
from jinja2 import Environment, PackageLoader, select_autoescape
import docutils
from docutils import core

from syntax.writer import HTML5Writer

import syntax.roles
import syntax.directives.annotations
import syntax.directives.statements

env = Environment(
    loader=PackageLoader('perso', 'template'),
    autoescape=select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True,
)

# TODO: move this the fuck away
CONTENT_DIR = 'content/'
BUILD_DIR = 'build/'

def main():
    """ Entry point for the `perso` static site builder. """
    parser = argparse.ArgumentParser(
            description="Build lescot's personal site.")
    subparsers = parser.add_subparsers()

    parser_build = subparsers.add_parser('build')
    parser_build.add_argument('--force', help='rebuild every file', action='store_true')
    parser_build.set_defaults(func=build)

    args = parser.parse_args()
    args.func(args)

def build(args):
    templates = {}

    os.makedirs(BUILD_DIR, exist_ok=True)

    # copy template static files to build dir
    if isdir('template/static/'):
        shutil.rmtree(join(BUILD_DIR, 'static/'), ignore_errors=True)
        shutil.copytree('template/static/', join(BUILD_DIR, 'static/'))


    for root, dirs, files in os.walk(CONTENT_DIR):
        for filename in files:
            if not filename.endswith('.rst'):
                continue

            src = join(root, filename)
            name, ext = os.path.splitext(filename)
            dst = join(BUILD_DIR, relpath(root, CONTENT_DIR), name + '.html')

            if not(args.force) and isfile(dst) and getmtime(dst) > getmtime(src):
                continue

            print("Building %s ..." % src)

            with open(src) as source:
                content = core.publish_parts(source = source.read(), writer = HTML5Writer())

                if 'template' in content['meta']:
                    template = content['meta']['template']
                else:
                    template = 'index'

                if template not in templates:
                    template = templates[template] = env.get_template(template + '.html')
                else:
                    template = templates[template]

                output = template.render(content = content['fragment'], **content['meta'])
                os.makedirs(os.path.dirname(dst), exist_ok=True)

                with open(dst, 'w+') as target:
                    target.write(output)

