#from lxml import etree
import xml.etree.ElementTree as etree
import sys
import common

ns = {'xs' : 'http://www.w3.org/2001/XMLSchema'}

tree = etree.parse(common.prepare_relative_path('cg_config.xsd'))
#root = tree.getroot()
elements = tree.findall(".//xs:element[@name='Configuration']/xs:complexType/xs:sequence/xs:element", ns)


#//element

print elements
header = '<?xml version="1.0" encoding="UTF-8"?>\n'

fin_config_nodes = []

#with open('/home/seymour/src/jinja2fromXSD/parse.jinja2', 'w') as fh:
#    fh.write(header)
#    fh.write("<Configuration>\n")
for el in elements:
    name_str = ""
    referenced_node = el.find("[@ref]")
    if referenced_node != None:
        element_name = referenced_node.attrib["ref"]
        path = ".//element[@name='{}']".format(element_name)
        node = tree.find(path, ns)
        if node != None:
            print node.attrib['name']
        fin_config_nodes.append(node)
    else:
        direct_node = el.find("[@name]")
        if direct_node != None:
            print direct_node.attrib['name']
    # if found an appropriate node add it to node list


    #fh.close()
# for node in fin_config_nodes:
#     if node != None:
#         print "Name: ", node.attrib['name']
