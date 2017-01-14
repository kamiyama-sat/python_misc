# -*- coding: utf-8 -*-
import sys
import os
import ntpath
import unicodedata


def find_all_files(directory):
	for root, dirs, files in os.walk(directory):
		yield root
		for file in files:
			yield os.path.join(root, file)


target_dir = "./"
if len(sys.argv) > 1:
	target_dir = sys.argv[1]


print("target_dir =", target_dir)
if not os.path.isdir(target_dir):
	print("ERROR:", target_dir, "is not dir!")


for file in find_all_files(target_dir):
	if os.path.isfile(file):
		dir, name = ntpath.split(file)
		normalized_name = unicodedata.normalize('NFC', name)
		if name != normalized_name:
			print(dir + "\\" + normalized_name)
			os.rename(file, dir + "\\" + normalized_name)
