import re
import urllib2


data = urllib2.urlopen("file:///C:/Users/aa/Documents/GitHub\May_Prac/google-python-exercises/babynames/baby1990.html")
new_file = data.read()
year = re.search(r'([\d]+)</h3', new_file)
print year.group(1)

def sort_names(name_number_tuple):
    return name_number_tuple[0]
                       
name_number = re.findall(r'<td>([\d]+)</td><td>([\w]+)</td><td>([\w]+)</td>', new_file)
#print name_number[0], name_number[1]
#print name_number
names_dictionary = {}
for i in range(len(name_number)):
    name = name_number[i][1]
    #print name
    number = name_number[i][0]
    names_dictionary[name] = name_number[i][0]
#print names_dictionary


arranged_names = sorted(names_dictionary.items(), key=sort_names)
for name in arranged_names:
    print name[0], name[1]
##    boy_names = name_number[i][1], name_number[i][0]
##    print boy_names
##    girl_names = name_number[i][2], name_number[i][0]
##    print girl_names


    
    #print name_number[i][2], name_number[i][0], name_number[i][1], name_number[i][0]



