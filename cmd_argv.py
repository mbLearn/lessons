import sys
import os
import commands

def List(dir):
    cmd = 'ls -l' + dir
    (status, output) = commands.getstatusoutput(cmd)
    print output
##    filenames = os.listdir(dir)
##    print filenames
##    for filename in filenames:
##        path = os.path.join(dir, filename)
##        print path
##        print os.path.abspath(path)
    
def main():
    List(sys.argv[1])

if __name__ == '__main__':
    main()


## new command
print ('\n')
print os.path.exists('/tmp/foo')


##import shutil
##shutil.copy(source, dest)
## it copies files. 

