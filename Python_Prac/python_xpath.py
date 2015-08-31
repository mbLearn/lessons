from xml.etree import ElementTree as ET
from io import StringIO
from collections import defaultdict

## 1
## extract the <value> entry which is just below the <name> entry marked 'swisspro'.
## I.e. I want to parse and extract the 'Q8H6N2' value.
import xml.etree.ElementTree as ET

data = """<parameters>
<parameter>
 <name>ec_num</name>
 <value>none</value>
 <units/>
 <url/>
 <id>2455</id>
 <m_date>2008-11-29 13:15:14</m_date>
 <user_id>24</user_id>
 <user_name>registry</user_name>
</parameter>
<parameter>
 <name>swisspro</name>
 <value>Q8H6N2</value>
 <units/>
</parameter>
</parameters>"""

tree = ET.fromstring(data)

for parameter in tree.iter(tag='parameter'):
    name = parameter.find('name')
    if name is not None and name.text == 'swisspro':
        print parameter.find('value').text, '\n'
        break


## 2
## To show the element as XML text, use the ElementTree.tostring() function:
root = ET.fromstring('''\
 <volume name="sp" type="span" operation="create">
     <driver>HDD1</driver>
     <driver>HDD2</driver>
     <driver>HDD3</driver>
     <driver>HDD4</driver>
 </volume>
 ''')
for nod in root.findall("./driver"):
    print ET.tostring(nod)
 
##<driver>HDD1</driver>
##
##<driver>HDD2</driver>
##
##<driver>HDD3</driver>
##
##<driver>HDD4</driver>


## 3

data = '''\
<keywords>
    <layer id="wheat">
        <layer id="indian">
            <keyword>chapati</keyword>
            <layer id="mumbai">
                <keyword>puri</keyword>
            </layer>
        </layer>
        <keyword>bread</keyword>
        <keyword>pita</keyword>
        <keyword>narn</keyword>
        <keyword>loaf</keyword>
    </layer>
    <layer id="fruit">
        <keyword>apple</keyword>
        <keyword>orange</keyword>
        <keyword>pear</keyword>
        <keyword>lemon</keyword>
    </layer>
</keywords>
'''

path = ['ROOT']  # stack for layer names
items = defaultdict(list)  # key=layer, value=list of items @ layer

f = StringIO(data)
for evt,e in ET.iterparse(f,('start','end')):
    if evt == 'start':
        if e.tag == 'layer':
            path.append(e.attrib['id']) # new layer added to path
        elif e.tag == 'keyword':
            items[path[-1]].append(e.text) # add item to last layer in path
    elif evt == 'end':
        if e.tag == 'layer':
            layer = path.pop()
            parent = path[-1]
            print layer,len(path),parent,items[layer]
