# Adds titles

from pathlib import Path, PurePath
import yaml
import os
from collections import defaultdict

def get_yaml(filename):
	s = ""
	delim_count = 0
	with open(filename, "r") as fh:
		s = fh.read()
		if s.find("categories:") == -1 or s.find("---") == -1:
			return "", "Badly formed"
		s = s[len("---"):]
		s = s[:s.find("---")]
		return s, None

def get_pages_for_categories():
	d = defaultdict(list)
	indir = Path("src")
	for f in indir.glob("*.md"):
		s_yaml, err = get_yaml(f)
		if err:
			continue
		yaml_tree = yaml.load(s_yaml, yaml.Loader)
		categories = yaml_tree["categories"]
		filename = str(f)[len("src/"):]
		for cat in categories:
			d[cat].append(filename)
	return d

outdir = "categories/"
d = get_pages_for_categories()
for key, value in d.items():
	filename = outdir + "category-" + key + ".rst"
	header = """
Header
======
.. toctree::
   :caption: Site Index:
   :maxdepth: 1
   
"""
	with open(filename, "w") as f:
		f.write(header)
		for line in value:		
			end = - len(".md")
			f.write("   " + line[:end] + "\n")
		# f.writelines(value)
