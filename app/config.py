# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import date
import os

__author__ = 'InG_byr'

version = '0.0.2'

buildtime = date.today()

data = {'version': version,
        'time': str(buildtime)}

base_dir = os.getcwd()

kwargs = {'output_dir': base_dir,
          'merge': True,
          'json_output': False,
          'caption': True}


def set_file_path(path):
    kwargs['output_dir'] = path


def set_file_itag(stream_id):
    kwargs['stream_id'] = stream_id


if __name__ == '__main__':
    with open('../version.json', 'w') as f:
        f.write(json.dumps(data))
