#1 How do I get a list of all files (and directories) in a given directory in Python?

import os

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

#2
