import os
import zipfile

from cldr import CLDR_VERSION, CLDR_FILE_COMMON

CLDR_URL = f'https://unicode.org/Public/cldr/{CLDR_VERSION}/{CLDR_FILE_COMMON}'
BASEDIR = os.path.dirname(os.path.realpath(__file__))

def has_data():
    '''Check if CLDR data has benn downloaded.'''
    data_dir = os.path.join(BASEDIR, 'data')
    data_path = os.path.join(data_dir, str(CLDR_VERSION), CLDR_FILE_COMMON)
    return os.path.isfile(data_path)

def download_data():
    data_dir = os.path.join(BASEDIR, 'data')
    version_dir = os.path.join(data_dir, str(CLDR_VERSION))
    zip_path = os.path.join(version_dir, CLDR_FILE_COMMON)

    os.system(f'mkdir -p {version_dir}')

    cmd = f'wget {CLDR_URL} -O {zip_path}'
    os.system(cmd)

def unzip_data():
    zip_path = os.path.join(BASEDIR, 'data', str(CLDR_VERSION),
        CLDR_FILE_COMMON)
    cldr_zip = zipfile.ZipFile(zip_path)
    cldr_zip.extractall(path=os.path.dirname(zip_path))
