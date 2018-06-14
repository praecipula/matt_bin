#!/usr/bin/env python
import sys
import re
import subprocess

match = re.search("(\d+)/list", sys.argv[1])
if match:
    print("List")
    print(match.group(1))
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate("/projects/" + match.group(1))
