import os
import xml.etree.ElementTree as ET

import data_utils
from cldr import CLDR_VERSION

DATA_DIR = os.path.join(data_utils.BASEDIR, 'data', str(CLDR_VERSION))
MAIN_DIR = os.path.join(DATA_DIR, 'common/main')

languages = [
    'root',
    'en',
    'ja',
    'ko',
]

locales = [
    'en_US',
    'en_UK',
    'ja_JP',
    'ko_KP',
    'ko_KR',
]


def locale_get_language(locale):
    language = locale.split('_')[0]
    if language not in languages:
        raise ValueError('No such language: ' + language)

    return language


class LdmlAttribute:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f'{self.key}="{self.value}"'


class LdmlNode:
    def __init__(self, path='/ldml'):
        self.path = path
        self.parent = None
        self.children = []
        self.text = None
        self.attributes = []

    def __str__(self):
        if self.text is not None:
            return f'<path="{self.path}" text="{self.text}">'
        return f'<path="{self.path}">'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def parse(language):
        tree = ET.parse(os.path.join(MAIN_DIR, f'{language}.xml'))
        root = tree.getroot()
        # Create LDML Node.
        ldml_node = LdmlNode()
        for child in root:
            # localeDisplayNames Node.
            if child.tag == 'localeDisplayNames':
                locale_display_names = LdmlNode(
                    path='/ldml/localeDisplayNames'
                )
                locale_display_names.parent = ldml_node
                ldml_node.children.append(locale_display_names)
                for ldp_child in child:
                    # languages Node.
                    if ldp_child.tag == 'languages':
                        languages = LdmlNode(
                            path='/ldml/localeDisplayNames/languages'
                        )
                        languages.parent = locale_display_names
                        locale_display_names.children.append(languages)
                        for langs_child in ldp_child:
                            # language Nodes.
                            if langs_child.tag == 'language':
                                language = LdmlNode(
                                    path='/ldml/localeDisplayNames/languages/language'
                                )
                                language.parent = languages
                                language.text = langs_child.text
                                for k, v in langs_child.attrib.items():
                                    attr = LdmlAttribute(k, v)
                                    language.attributes.append(attr)
                                languages.children.append(language)

        return ldml_node