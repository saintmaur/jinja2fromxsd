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
        path = ".//xs:element[@name='{}']".format(element_name)
        node = tree.find(path, ns)
        if node != None:
            fin_config_nodes.append(node)
    else:
        fin_config_nodes.append(el)
    # if found an appropriate node add it to node list


def get_attributes(attrs):
    for attr in attrs:
        print attr.attrib['name']

def get_children(node):
    # if not empty, argument path should end with '/'
    # otherwise no magic is guaranteed =)
    temp_config = dict()
    ct_path = ".//xs:complexType"
    els_path = ".//xs:element"
    attr_path = ".//xs:attribute"
    complex_type = node.find(ct_path, ns)

    if complex_type is not None:
        temp_config[node.attrib['name']] = dict()
        attrs = complex_type.findall(attr_path, ns)
        if attrs is not None:
            temp_config[node.attrib['name']]['attribs'] = []
            for attr in attrs:
                temp_config[node.attrib['name']]['attribs'].append(attr.attrib['name'])

        children = complex_type.findall(els_path , ns)
        if children is not None:
            temp_config[node.attrib['name']]['children'] = []
            for child in children:
                print "=========="
                print child.attrib['name']
                print "=========="
                temp_config[node.attrib['name']]['children'].\
                    append(get_children(child))
    return temp_config

    #fh.close()

config = []
for node in fin_config_nodes:
    ct_path = "xs:complexType"
    el_seq_path = "xs:sequence"
    attr_path = "xs:attribute"
    if node != None:
        config.append(get_children(node))

print config