#!/usr/bin/env python
import os
from argparse import ArgumentParser

import data_utils
import locale_utils

TEMPLATES_DIR = os.path.realpath(os.path.join(
    data_utils.BASEDIR, '../../templates'))

templates = [
    {
        'name': 'locale-enum',
        'file': 'locale_enum.rs',
    },
]

def gen_locale_enum(template_file):
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    f = open(template_path, 'r')
    template = f.read()
    f.close()

    locales = ''
    for locale in locale_utils.locales:
        locales += '    ' + locale.title().replace('_', '') + ',\n'
    locales = locales.rstrip()

    ret = template.format(locales)

    return ret

def gen(template):
    found = next((t for t in templates if t['name'] == template), None)
    if found is None:
        raise ValueError(template + ': No such template.')
    if found['name'] == 'locale-enum':
        print(gen_locale_enum(found['file']))

def ls():
    print(''' - available templates
locale-enum
    ''')

if __name__ == '__main__':
    if not data_utils.has_data():
        data_utils.download_data()
        data_utils.unzip_data()

    argp = ArgumentParser(
        prog='./cldr-tool.py',
        description='Eshu CLDR tool.'
    )
    sub_argp = argp.add_subparsers(dest='subcommand', help='Sub-commands')
    # Sub-command 'gen'
    argp_gen = sub_argp.add_parser('gen',
        help='Generate code from templates')
    argp_gen.add_argument('template', type=str,
        help='Template to generate code.')
    # Sub-command 'ls'
    argp_ls = sub_argp.add_parser('ls',
        help='List all available templates.')

    args = argp.parse_args()

    if args.subcommand == 'gen':
        gen(args.template)
    elif args.subcommand == 'ls':
        ls()

