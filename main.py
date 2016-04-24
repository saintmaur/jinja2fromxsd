#from lxml import etree
import xml.etree.ElementTree as etree
import sys

ns = {'xs' : 'http://www.w3.org/2001/XMLSchema'}

tree = etree.parse('/home/seymour/src/jinja2fromXSD/cg_config.xsd')
#root = tree.getroot()
elements = tree.findall(".//xs:element[@name='Configuration']/xs:complexType/xs:sequence/xs:element", ns)


#//element

print elements
header = '<?xml version="1.0" encoding="UTF-8"?>\n'


with open('/home/seymour/src/jinja2fromXSD/parse.jinja2', 'w') as fh:
    fh.write(header)
    fh.write("<Configuration>\n")
    for el in elements:
        name_str = ""
        name = el.find("[@ref]")
        if name != None:
            name_str = name.attrib["ref"]
            #print name.attrib["ref"]
        else:
            name = el.find("[@name]")
            if name != None:
                name_str = name.attrib["name"]
                #print name.attrib["name"]
        print "Name:", name_str
        fh.write(name_str+"\n")
    fh.close()