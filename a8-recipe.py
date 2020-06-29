#!/usr/bin/env python

import os
import subprocess
import sys

version="2.6.0-1708282016"

repoSettingsFile = os.path.join(os.path.expanduser("~"), ".a8/repo.properties")
repoSettingsLines = open(repoSettingsFile, 'r').readlines()

settings = []
for line in repoSettingsLines:
  l = line.split("=")
  if len(l) == 2:
    settings.append([l[0].strip(), l[1].strip()])

def prop(name):
  for e in settings:
    if e[0] == name:
        return e[1]
  raise "no property named " + name + " found in " + repoSettingsFile

def dir(*path_parts):
  return os.path.realpath(os.path.join(*path_parts))

def parent_dir(d):
  return os.path.dirname(d)

script_file = dir(__file__)
script_dir = parent_dir(script_file)
packages_dir = parent_dir(script_dir)
tools_dir = parent_dir(packages_dir)

repo_password = prop('repo_password')
repo_user = prop('repo_user')
repo_url = prop('repo_url')


repo_url_split_index = repo_url.index("://") + 3
repo_url_prefix = repo_url[0: repo_url_split_index]
repo_url_suffix = repo_url[repo_url_split_index: ]

resolved_repo_url = repo_url_prefix + repo_user + ":" + repo_password + "@" + repo_url_suffix

args = (
  [
    script_dir + "/coursier",
    "launch",
    "-r", 
    resolved_repo_url,
    "-M", 
    "a8.recipe.RecipeMain",
    "a8:a8-recipe:" + version,
    "--",
  ] + 
  sys.argv[1:] +
  [ "--tools-dir=" + tools_dir]
)

#print " ".join(args)

subprocess.call(args)
