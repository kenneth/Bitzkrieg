#!/usr/bin/python3 
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.FIX50SP2 import Tag, Component, RepeatingGroup, Message
from datetime import datetime

def update_sendingtime(msg, hopcompid=''):
    if hopcompid == '':
        msg.Header.SendingTime.value = datetime.utcnow()
    else:
        hop_group = Fix.Components.HopGrp.NoHops()
        hop_group.HopSendingTime.value = datetime.utcnow()
        hop_group.HopCompID.value = hopcompid
        msg.Header.HopGrp.groups.append(hop_group)

def fixmsg2dict(msg):
    if isinstance(msg, RepeatingGroup):
        ret = []
        for group in msg.groups:
            ret.append(fixmsg2dict(group))
            
        return ret
    elif isinstance(msg, Message) or isinstance(msg, Component) or isinstance(msg, Fix.Header):
        ret = {}
        for name, attr in msg.__dict__.items():
            ret[name] = fixmsg2dict(attr)
            
        return ret
    elif isinstance(msg, Tag):
        return msg.value
    elif isinstance(msg, bool):
        pass
    else:
        assert False, "Unknow type %s" % msg.__class__.__name__    