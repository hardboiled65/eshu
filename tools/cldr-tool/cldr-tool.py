#!/usr/bin/env python
import os

import data_utils

if __name__ == '__main__':
    if not data_utils.has_data():
        data_utils.download_data()
        data_utils.unzip_data()
