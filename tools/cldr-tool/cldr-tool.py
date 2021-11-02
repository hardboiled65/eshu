#!/usr/bin/env python
import os
from argparse import ArgumentParser

import data_utils
import locale_utils
from locale_utils import LdmlNode

TEMPLATES_DIR = os.path.realpath(os.path.join(
    data_utils.BASEDIR, '../../templates'))

templates = [
    {
        'name': 'language-enum',
        'file': 'language_enum.rs',
    },
    {
        'name': 'script-enum',
        'file': 'script_enum.rs',
    },
    {
        'name': 'locale-enum',
        'file': 'locale_enum.rs',
    },
    {
        'name': 'locale-new',
        'file': 'locale_new.rs',
    },
    {
        'name': 'locale-language',
        'file': 'locale_language.rs',
    },
    {
        'name': 'locale-territory',
        'file': 'locale_territory.rs',
    },
]

#========================
# Utility functions
#========================

def locale_to_rust_enum(locale):
    return locale.title().replace('_', '')

def language_to_rust_enum(language):
    return language.title()

def territory_to_rust_enum(territory):
    if territory[0].isnumeric():
        return f'Code{territory}'
    return territory.title()

def get_template(template_file):
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    f = open(template_path, 'r')
    template = f.read()
    f.close()

    return template

#========================
# Generate functions
#========================

def gen_language_enum(template_file):
    template = get_template(template_file)

    ldml = LdmlNode.parse('en')
    languages = ldml.find_by_path('/ldml/localeDisplayNames/languages')

    lang_list = []
    def get_lang(lang_type):
        if lang_type.count('_') > 0:
            return lang_type.split('_')[0]
        return lang_type
    for language in languages.children:
        lang = get_lang(language.attribute_value('type'))
        filtered = filter(
            lambda x: get_lang(x.attribute_value('type')) == lang, lang_list
        )
        if len(list(filtered)) > 0:
            continue
        lang_list.append(language)

    # Indent enum values.
    txt = ''
    for language in lang_list:
        txt += '    /// ' + language.text + '\n'
        txt += f'    {language_to_rust_enum(language.attribute_value("type"))},\n'
    # Remove trailing newline.
    txt = txt.rstrip()

    ret = template.format(txt)

    return ret

def gen_script_enum(template_file):
    template = get_template(template_file)

    ldml = LdmlNode.parse('en')
    scripts = ldml.find_by_path('/ldml/localeDisplayNames/scripts')
    print(scripts) # DEBUG!

    sc_list = []
    def get_sc(sc_type):
        return

    # Indent enum values.
    txt = ''
    for sciprt in sc_list:
        txt += ''
    # Remove trailing newline.
    txt = txt.rstrip()

    ret = template.format(txt)

    return ret

def gen_locale_enum(template_file):
    template = get_template(template_file)

    locales = ''
    for locale in locale_utils.locales:
        locales += '    ' + locale_to_rust_enum(locale) + ',\n'
    locales = locales.rstrip()

    ret = template.format(locales)

    return ret

def gen_locale_new(template_file):
    template = get_template(template_file)

    matches = ''
    for locale in locale_utils.locales:
        matches += '            '
        matches += f'"{locale}"'
        matches += f' => Ok(Locale::{locale_to_rust_enum(locale)})'
        matches += ',\n'
    matches = matches.rstrip()

    ret = template.format(matches)

    return ret

def gen_locale_language(template_file):
    template = get_template(template_file)

    matches = ''
    for locale in locale_utils.locales:
        language = locale_utils.locale_get_language(locale)
        matches += '            '
        matches += f'Locale::{locale_to_rust_enum(locale)}'
        matches += f' => "{language}"'
        matches += ',\n'
    matches = matches.rstrip()

    ret = template.format(matches)

    return ret

def gen_locale_territory(template_file):
    template = get_template(template_file)

    matches = ''
    for locale in locale_utils.locales:
        territory = locale_utils.locale_get_territory(locale)
        matches += '            '
        matches += f'Locale::{locale_to_rust_enum(locale)}'
        matches += f' => "{territory}"'
        matches += ',\n'
    matches = matches.rstrip()

    ret = template.format(matches)

    return ret

#=================
# Sub-commands
#=================

def gen(template):
    found = next((t for t in templates if t['name'] == template), None)
    if found is None:
        raise ValueError(template + ': No such template.')
    if found['name'] == 'locale-enum':
        print(gen_locale_enum(found['file']))
    elif found['name'] == 'locale-new':
        print(gen_locale_new(found['file']))
    elif found['name'] == 'locale-language':
        print(gen_locale_language(found['file']))
    elif found['name'] == 'locale-territory':
        print(gen_locale_territory(found['file']))
    elif found['name'] == 'language-enum':
        print(gen_language_enum(found['file']))
    elif found['name'] == 'script-enum':
        print(gen_script_enum(found['file']))

def ls():
    print(''' - available templates
language-enum
script-enum
locale-enum
locale-new
locale-language
locale-territory
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

