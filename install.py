#!/usr/bin/python

import os
from os.path import expanduser
import subprocess


def makedirs(dir):
  if not os.path.exists(dir):
    print("mkdir " + dir)
    os.makedirs(dir)


def run(args):
  print("running " + str(args))
  subprocess.call(args)


def dir(*parts):
  return os.path.realpath(os.path.join(*parts))


tools_dir = dir(expanduser("~"), "tools-a8")
packages_dir = dir(tools_dir, "packages")
a8_recipe_dir = dir(packages_dir, "/a8-recipe")
bin_dir = dir(tools_dir, "bin")
a8_recipe_exec = dir(bin_dir, "a8-recipe")


makedirs(bin_dir)


def main():
  # symlink the a8-recipe.py to the bin folder
  if os.path.exists(a8_recipe_exec):
    os.remove(a8_recipe_exec)
  print "creating symlink " + a8_recipe_exec
  os.symlink("../packages/a8-recipe/a8-recipe.py", a8_recipe_exec)

  # run the a8-recipe init
  run([a8_recipe_exec, "init"])


if __name__ == "__main__":
    main()


