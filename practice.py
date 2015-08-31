from sys import argv
import re
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

       

