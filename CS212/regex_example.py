import re
def Find(pattern, text):
    match = re.search(pattern, text)
    if match: return match.group()
    else: return 'not found'


string1 = "my email address is .blah.blah@gmail.com and hurry.hooray@gmail.com yadda @."

print Find(r'\w[\w.]*@[\w.]+', string1) #blah.blah@gmail.com
print Find(r'[\w.]*@[\w.]+', string1)   #.blah.blah@gmail.com
print re.findall(r'[\w.]+@[\w.]+', string1) #['.blah.blah@gmail.com', 'hurry.hooray@gmail.com']
print re.findall(r'([\w.]+)@([\w.]+)', string1) #[('.blah.blah', 'gmail.com'), ('hurry.hooray', 'gmail.com')]


string2 = "my email address is nick.pat@gmail.com yadda@."
a = re.search(r'[\w]+@[\w]+', string2)
print a.group() #pat@gmail # shows why we are using [\w.]
m = re.search(r'([\w.]+)@([\w.]+)', string2)
print m.group()
print m.group(1)

# you call the re.search, once you find the match object and if you want to
# extract certain info you use group(N), N stands for no.

