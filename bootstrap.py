#!/usr/bin/python

import os
from os.path import expanduser
import subprocess


def makedirs(dir):
  if not os.path.exists(dir):
    print "mkdir " + dir
    os.makedirs(dir)


def git_clone_a8_recipes():
  run(["git", "clone", "https://gitlab.accur8.io/a8/recipe.git", a8_recipe_dir])


def run(args):
  print "running " + str(args)
  subprocess.call(args)


user_home = dir(expanduser("~"))


def dir(path_parts*):
  return os.path.realpath(os.path.join(path_parts))


tools_dir = dir(user_home, "tools-a8")
packages_dir = dir(tools_dir, "packages")
a8_recipe_dir = dir(packages_dir, "a8-recipe")
bin_dir = dir(tools_dir, "bin")


makedirs(a8_recipe_dir)
makedirs(bin_dir)


# run git clone
git_clone_a8_recipes()

# run the installer
run([a8_recipe_dir + "/install.py"])


