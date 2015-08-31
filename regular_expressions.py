from sys import argv
import re, urllib
##
##script = argv
##user_name = argv
##prompt = '> '
##
##print "Hi %s, I'm the %s script." %(user_name, script)
##print "Do you like me %s?" %user_name
##likes = raw_input(prompt)
##print "Where do you live %s?" %user_name
##lives = raw_input(prompt)
##
##print """
##Alright, so you said %r about liking me.
##You live in %r. Not sure where that is.
##""" %(likes, lives)

## Regular Expressions.

m = (re.split(r'\s*', 'here are some words'))
print m

x = re.findall(r'([\w.]+)@([\w.]+)', 'abc@gmail.com is xyz@yahoo.com and rxw@hotmail.com')
print x

y = re.findall(r'[\w.]+@[\w.]+', 'abc@gmail.com is xyz@yahoo.com and rxw@hotmail.com')
print y

x = re.split(r'[a-fA-F0-9p-q]', 'dsjfhwehruwiefjsdkajloajdoqSALKSDJAOWEIJFWA', re.I|re.M)
print x

x = re.split(r'[a-fA-F0-9p-q]', 'dsjfhwehruwiefjsdkajloajdoqSALKSDJAOWEIJFWA')
print x

x = re.split(r'[a-f][a-f]', 'dsjfhwecruwiefjsdkajloajdoqSAeKSDJAOWEIJFWA', re.I|re.M)
print x


x = re.findall(r'\d+', 'addsadas324 main street.dsfsdfs')
print x

# {1,5} => search for minimum of 1 and mx. of 5 digits
# \. , extracts eaxctly .(period)
x = re.findall(r'\d{1,5}\s\w+\s\w+\.', 'addsadas3245 main street.dsfsdfs') 
print x

## New Problem - Find internet sites and titles
try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn msn'. split()
pat = re.compile(r'<title>+.*</title>+', re.I|re.M)

for s in sites:
    print ('Searching: ' + s)
    try:
        u = urllib.urlopen('http://'+s+'.com')
    except:
        u = urllib.request.urlopen('http://'+s+ '.com')
    text = u.read()
    title = re.findall(pat, str(text))
    print (title[0])
print ('\n')


## New Problem - Extract data from files
## read the first half-dozen data records from two files
## use regular expressions - A pattern string can match

readings = []
for filename in ('M:/Regex/data-1.txt', 'M:/Regex/data-2.txt'):
    lines = open(filename, 'r').read().strip().split('\n')
    #print lines
    readings += lines[3:9]

for r in readings:
    print r

# selcet readings in month '06' or month '07' - without using ReGex
for r in readins:
    if ('06' in r) or ('07' in r):
        print r


              
