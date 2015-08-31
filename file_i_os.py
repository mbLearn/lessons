import os, re, sys

def walkdir(dirname):
    for root, _dirs, filenames in os.walk(dirname):
        path = root.split('/')
        print (len(path) - 1) * '---', os.path.basename(root)
        print filenames
        for filename in filenames:
            print filename
            new_path = os.path.join(dirname, filename)
            abs_path = os.path.abspath(new_path)
            print abs_path
            f = (open(abs_path, 'r')).read()
            #print f.read()
            match_word = re.findall(r'(and [A-Z a-z]+)', f)
            print match_word
            


print walkdir('M:/Sample') 

def new_lst(dir):
    for root, subs, filenames in os.walk(dir):
##        print root
##        print subs
##        print filenames
        for filename in filenames:
            path = os.path.join(dir, filename)
            abs_path = os.path.abspath(path)
            print abs_path
##          for path in filename:
            f = (open(abs_path, 'r')).read()
            #print f.read()
            match_word = re.findall(r'(and [A-Z a-z]+)', f)
            print match_word

def Lst(dir):
    filenames = os.listdir(dir)
    print filenames
    for filename in filenames:
        path = os.path.join(dir, filename)
        abs_path = os.path.abspath(path)
        print abs_path
##        for path in filename:
        f = (open(abs_path, 'r')).read()
        #print f.read()
        match_word = re.findall(r'(and [A-Z a-z]+)', f)
        print match_word
            
          

#----------------------------------------------------------------
## Failed attempts
# ---------------------------------------------------------------
##try:
##    for each_file in os.listdir("M:.."):
##        f = open(each_file, 'r')
##        match_word = re.findall(r'(and[A-Z][a-z]+)', f)
##        print match_word
##except IOError:
##    pass
##
##
##for each_file in (os.listdir('M:/sample')):
##	f = open(each_file, 'r')
##	for i in f.readlines():
##		#print i
##		match = re.findall(r'(the[A-Za-z]+\.)', i)
##		print match
