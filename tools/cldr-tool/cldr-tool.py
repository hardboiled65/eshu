#!/usr/bin/env python
import os

import data_utils

TEMPLATES_DIR = os.path.realpath(os.path.join(
    data_utils.BASEDIR, '../../templates'))

if __name__ == '__main__':
    if not data_utils.has_data():
        data_utils.download_data()
        data_utils.unzip_data()

    print(TEMPLATES_DIR)
