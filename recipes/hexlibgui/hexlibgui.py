#!/usr/bin/python

import os
import sys
import subprocess

script_file = os.path.realpath(__file__)
script_dir = os.path.dirname(script_file)

os.chdir(script_dir)

args = ["java", "-jar", "HexLibGUI.jar"] + sys.argv[1:]

print args

os.execvp("java", args)

