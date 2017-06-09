#!/usr/bin/python

import os
from os.path import expanduser
import subprocess


def makedirs(d):
  if not os.path.exists(d):
    print "mkdir " + d
    os.makedirs(d)


def git_clone_a8_recipes():
  run(["git", "clone", "https://github.com/fizzy33/a8-recipe", a8_recipe_dir])


def run(args):
  print "running " + str(args)
  subprocess.call(args)


def directory(*path_parts):
  return os.path.realpath(os.path.join(*path_parts))


user_home = directory(expanduser("~"))

tools_dir = directory(user_home, "tools-a8")
packages_dir = directory(tools_dir, "packages")
a8_recipe_dir = directory(packages_dir, "a8-recipe")
bin_dir = directory(tools_dir, "bin")


makedirs(a8_recipe_dir)
makedirs(bin_dir)


# run git clone
git_clone_a8_recipes()

# run the installer
run([a8_recipe_dir + "/install.py"])
