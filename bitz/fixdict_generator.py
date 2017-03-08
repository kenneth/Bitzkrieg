#!/usr/bin/python3  
import xml.etree.ElementTree
import re

def tab(str="", indents = 0):
    return '    ' * indents + str + "\n"
    
def get_valid_name(name):
    if re.match("^[0-9]+.*$", name) is not None:
        return "N" + name
    else:
        return name
        
def get_required(value):
    if value == 'Y':
        return 'True'
    else:
        return 'False'

def generate_basic_classes(beginning_indents):
    ret = ""
    # Generate the base element
    ret += tab()
    ret += tab()
    ret += tab("class BaseElement(object):", beginning_indents)
    ret += tab("def __init__(self, required=False):", beginning_indents + 1)
    ret += tab("self.required = required", beginning_indents + 2)
    
    # Generate the tag class
    ret += tab()
    ret += tab()
    ret += tab("class Tag(BaseElement):", beginning_indents)
    ret += tab("def __init__(self, value=None, required=False):", beginning_indents + 1)
    ret += tab("BaseElement.__init__(self, required=required)", beginning_indents + 2)
    ret += tab("self.value = value", beginning_indents + 2)
    
    # Generate the component class
    ret += tab()
    ret += tab()
    ret += tab("class Component(BaseElement):", beginning_indents)
    ret += tab("def __init__(self, required=False):", beginning_indents + 1)
    ret += tab("BaseElement.__init__(self, required=required)", beginning_indents + 2)
    
    # Generate the group class
    ret += tab()
    ret += tab()
    ret += tab("class Group(Component):", beginning_indents)
    ret += tab("def __init__(self, required=False):", beginning_indents + 1)
    ret += tab("Component.__init__(self, required=required)", beginning_indents + 2)
    
    # Generate the repeating group class
    ret += tab()
    ret += tab()
    ret += tab("class RepeatingGroup(Component):", beginning_indents)
    ret += tab("def __init__(self, required=False):", beginning_indents + 1)
    ret += tab("Component.__init__(self, required=required)", beginning_indents + 2)
    ret += tab("self.groups = []", beginning_indents + 2)
    
    # Generate the message class
    ret += tab()
    ret += tab()
    ret += tab("class Message(object):", beginning_indents)
    ret += tab("def __init__(self):", beginning_indents + 1)
    ret += tab("pass", beginning_indents + 2)
    
    # Generat the application message class
    ret += tab()
    ret += tab()
    ret += tab("class AppMessage(Message):", beginning_indents)
    ret += tab("def __init__(self):", beginning_indents + 1)
    ret += tab("Message.__init__(self)", beginning_indents + 2)
    
    return ret

def generate_fields(version, root, beginning_indents):
    ret = ""
    fields = root.find('fields')
    
    ret += tab("class Tags:", beginning_indents)
    beginning_indents += 1
    
    for field in fields.findall('field'):
        number = field.get('number')
        name = get_valid_name(field.get('name'))
        type = field.get('type')
        
        ret += tab("class %s(Tag):" % (name), beginning_indents)
        ret += tab("Tag = %s" % number, beginning_indents + 1)
        ret += tab("Type = \"%s\"" % type, beginning_indents + 1)
        
        values = field.findall('value')
        if len(values) > 0:
            ret += tab("class Values:", beginning_indents + 1)
            assert type in ["CHAR", "STRING", "INT", "NUMINGROUP", 
                            "MULTIPLECHARVALUE", "BOOLEAN", "MULTIPLESTRINGVALUE"], \
                   "Invalid type %s" % type
                   
            for value in values:
                description = get_valid_name(value.get('description'))
                enum_value = value.get('enum')
                if type in ['INT', 'NUMINGROUP']:
                    ret += tab("%s = %s" % (description, enum_value), beginning_indents + 2)
                elif type == 'BOOLEAN':
                    ret += tab("%s = %d" % (description, 1 if enum_value == 'Y' else 0), 
                               beginning_indents + 2)
                else:
                    ret += tab("%s = \"%s\"" % (description, enum_value), beginning_indents + 2)
                    
        ret += tab()
        
    return ret
    
def generate_components(version, root, beginning_indents):
    ret = ""
    components = root.find('components')
    components = sorted(components, key=lambda x: len(x.findall('component') \
                                                      if x.find('group') is None \
                                                      else x.find('group').findall('component')))
    ret += tab("class Components:", beginning_indents)
    beginning_indents += 1
    
    for component in components:
        component_name = component.get('name')
        if component.find('group') is None:
            # Single component
            ret += tab("class %s(Component):" % component_name, beginning_indents)
            ret += tab("def __init__(self, required=False):", beginning_indents + 1)
            ret += tab("Component.__init__(self, required=required)", beginning_indents + 2)
            current_indents = beginning_indents + 2
        else:
            # Repeat group. Assume only one group in the componenet
            assert len(component.findall('group')) == 1, \
                    "Assume only one group in the component"
            component = component.find('group')
            ret += tab("class %s(RepeatingGroup):" % component_name, beginning_indents)
            group_name = component.get('name')
            ret += tab("class %s(Group):" % group_name, beginning_indents + 1)
            ret += tab("def __init__(self, required=False):", beginning_indents + 2)
            ret += tab("Group.__init__(self, required=required)", beginning_indents + 3)
            current_indents = beginning_indents + 3
            
        for field in component.findall('field'):
            field_name = field.get('name')
            field_required = get_required(field.get('required'))
            ret += tab("self.%s = %s.Tags.%s(required=%s)" % \
                        (field_name, version, field_name, field_required), 
                        current_indents)
        
        for subcomponent in component.findall('component'):
            subcomponent_name = subcomponent.get('name')
            subcomponent_required = get_required(subcomponent.get('required'))
            ret += tab("self.%s = %s.Components.%s(required=%s)" % \
                        (subcomponent_name, version, subcomponent_name, subcomponent_required), 
                        current_indents)
        
        ret += tab()
            
    return ret

def generate_headers(version, root, beginning_indents):
    ret = ""
    header = root.find('header')
    ret += tab("class Header:", beginning_indents)
    ret += tab("def __init__(self):", beginning_indents + 1)
    
    for field in header.findall('field'):
        field_name = field.get('name')
        field_required = get_required(field.get('required'))
        ret += tab("self.%s = %s.Tags.%s(required=%s)" % \
                    (field_name, version, field_name, field_required), 
                    beginning_indents + 2)
        
    for subcomponent in header.findall('component'):
        subcomponent_name = subcomponent.get('name')
        subcomponent_required = get_required(subcomponent.get('required'))
        ret += tab("self.%s = %s.Components.%s(required=%s)" % \
                    (subcomponent_name, version, subcomponent_name, subcomponent_required), 
                    beginning_indents + 2)
    
    return ret
    
def generate_messages(version, root, beginning_indents):
    ret = ""
    messages = root.find('messages')
    messages = messages.findall('message')
    ret += tab("class Messages:", beginning_indents)
    beginning_indents += 1    
    
    for message in messages:
        message_name = message.get('name')
        message_type = message.get('msgtype')
        message_cat = ("AppMessage" if message.get('msgcat') == 'app' else 'SessionMessage')
        
        ret += tab("class %s(%s):" % (message_name, message_cat), beginning_indents)
        ret += tab("MsgType = \"%s\"" % message_type, beginning_indents + 1)
        ret += tab("def __init__(self):", beginning_indents + 1)
        ret += tab("self.Header = %s.Header()" % version, beginning_indents + 2)
        ret += tab("self.Header.MsgType.value = \"%s\"" % message_type, beginning_indents + 2)
        
        for field in message.findall('field'):
            field_name = field.get('name')
            field_required = get_required(field.get('required'))
            ret += tab("self.%s = %s.Tags.%s(required=%s)" % \
                        (field_name, version, field_name, field_required), 
                        beginning_indents + 2)
        
        for subcomponent in message.findall('component'):
            subcomponent_name = subcomponent.get('name')
            subcomponent_required = get_required(subcomponent.get('required'))
            ret += tab("self.%s = %s.Components.%s(required=%s)" % \
                        (subcomponent_name, version, subcomponent_name, subcomponent_required), 
                        beginning_indents + 2)
                        
        ret += tab()
    
    return ret
    
if __name__ == '__main__':
    header_file_name = 'FIXT11.xml'
    file_name = 'FIX50SP2.xml'
    version = file_name.replace('.xml', '')
    root = xml.etree.ElementTree.parse(file_name).getroot()
    header_root = xml.etree.ElementTree.parse(header_file_name).getroot()
    
    beginning_indents = 0
    ret = tab("#!/usr/bin/python3", beginning_indents)
    ret += generate_basic_classes(beginning_indents)
    
    # Generate the version
    ret += tab()
    ret += tab()
    ret += tab("class %s:" % version, beginning_indents)
    beginning_indents += 1
    
    # Generate fields
    ret += generate_fields(version, root, beginning_indents)
    
    # Generate groups
    ret += tab()
    ret += generate_components(version, root, beginning_indents)
    
    # Generate headers
    ret += tab()
    ret += generate_headers(version, header_root, beginning_indents)
    
    # Generate messages
    ret += tab()
    ret += generate_messages(version, root, beginning_indents)
    
    
    f = open('%s.py' % version, 'w+')
    f.write(ret)
    f.close()