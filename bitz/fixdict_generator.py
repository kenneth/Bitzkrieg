#!/usr/bin/python3  
import xml.etree.ElementTree
import re

def tab(str, indents = 0):
    return '    ' * indents + str
    
def get_valid_name(name):
    if re.match("^[0-9]+.*$", name) is not None:
        return "N" + name
    else:
        return name

if __name__ == '__main__':
    file_name = 'FIX50SP2.xml'
    root = xml.etree.ElementTree.parse(file_name).getroot()
    fields = root.find('fields')
    
    beginning_indents = 0
    ret = tab("#!/usr/bin/python3\n", beginning_indents)
    ret += tab("class %s:\n\n" % file_name.replace('.xml', ''), beginning_indents)
    
    beginning_indents += 1
    ret += tab("class Tags:\n\n", beginning_indents)
    
    beginning_indents += 1
    for field in fields.findall('field'):
        number = field.get('number')
        name = get_valid_name(field.get('name'))
        type = field.get('type')
        
        ret += tab("class %s:\n" % name, beginning_indents)
        ret += tab("Tag = %s\n" % number, beginning_indents + 1)
        ret += tab("Type = \"%s\"\n" % type, beginning_indents + 1)
        
        values = field.findall('value')
        if len(values) > 0:
            ret += tab("class Values:\n", beginning_indents + 1)
            assert type in ["CHAR", "STRING", "INT", "NUMINGROUP", 
                            "MULTIPLECHARVALUE", "BOOLEAN", "MULTIPLESTRINGVALUE"], \
                   "Invalid type %s" % type
                   
            for value in values:
                description = get_valid_name(value.get('description'))
                enum_value = value.get('enum')
                if type in ['INT', 'NUMINGROUP']:
                    ret += tab("%s = %s\n" % (description, enum_value), beginning_indents + 2)
                elif type == 'BOOLEAN':
                    ret += tab("%s = %d\n" % (description, 1 if enum_value == 'Y' else 0), 
                               beginning_indents + 2)
                else:
                    ret += tab("%s = \"%s\"\n" % (description, enum_value), beginning_indents + 2)
        
        ret += tab("\n", 0)
    
    f = open('%s.py' % file_name.replace('.xml', ''), 'w+')
    f.write(ret)
    f.close()