#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

def get_script_path():
    path = os.path.dirname(sys.argv[0])
    if(path != ''):
        return os.path.dirname(sys.argv[0]) + "/"
    else:
        return ''