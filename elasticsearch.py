#!/usr/bin/python

import subprocess
import os
import re

file_dir = "/etc/elasticsearch/"
file = "elasticsearch.yml"
full_file = file_dir + file

backup_cmd = "python file_backup.py " + full_file + " " + file_dir
p = subprocess.Popen(backup_cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)

findlines = open(full_file).read().split('\n')
replacelines = open('elasticsearch.txt').read().split('\n')
find_replace = dict(zip(findlines, replacelines))


with open(full_file, "w") as data:
        for line in data:
            for key in find_replace:
                if key in line:
                    lines = re.sub(key, find_replace[key], full_file)
