#!/usr/bin/python

import os
import sys
import subprocess

script_file = os.path.realpath(__file__)
script_dir = os.path.dirname(script_file)

os.chdir(script_dir)

args = ["sh", "jvmtop.sh"] + sys.argv[1:]

os.execvp("sh", args)

