#!/usr/bin/env python

import os
import subprocess
import sys
import xml.etree.ElementTree

mavenSettingsFile = os.path.join(expanduser("~"), ".m2/settings.xml")
mavenSettings = xml.etree.ElementTree.parse(mavenSettingsFile).getroot().find('servers').find('server')

version="2.0.52-1611141017"

def dir(*path_parts):
  return os.path.realpath(os.path.join(*path_parts))

def parent_dir(d):
  return os.path.dirname(d)

script_file = dir(__file__)
script_dir = parent_dir(script_file)
packages_dir = parent_dir(script_dir)
tools_dir = parent_dir(packages_dir)

password = mavenSettings.find('password').text
username = mavenSettings.find('username').text

args = (
  [
    script_dir + "/coursier",
    "launch",
    "-r", 
    "https://" + username + ":" + password + "@accur8.artifactoryonline.com/accur8/all/",
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
