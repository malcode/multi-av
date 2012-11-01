#/usr/bin/env python
import subprocess

process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
result =  process.communicate()[0]

