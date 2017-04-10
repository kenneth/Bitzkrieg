#!/usr/bin/python3 
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.FIX50SP2 import Tag, Component, RepeatingGroup, Message
from datetime import datetime

def update_fixtime(msg, tag, hopcompid='', now_time=None):
    if tag == Fix.Tags.SendingTime.Tag:
        msg.Header.SendingTime.value = datetime.utcnow() if now_time is None else now_time
    elif tag == Fix.Tags.TransactTime.Tag:
        msg.TransactTime.value = datetime.utcnow() if now_time is None else now_time
    elif tag == Fix.Tags.HopSendingTime.Tag and hopcompid != '':
        hop_group = Fix.Components.HopGrp.NoHops()
        hop_group.HopSendingTime.value = datetime.utcnow() if now_time is None else now_time
        hop_group.HopCompID.value = hopcompid
        msg.Header.HopGrp.groups.append(hop_group)
    else:
        assert False, "Invalid input. Tag = %s. HopCompId = %s" % \
            (tag, hopcompid)

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