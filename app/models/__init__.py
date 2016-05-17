from Users import Users
from Role import Role
from Session import Session
from cqlengine.management import sync_table
from cqlengine import connection

def toDict(model, convertstring = False):
    _keys = model._values.keys()
    _ret = {}
    for _key in _keys:
        if convertstring:
	       _ret[_key] = unicode(getattr(model,_key))
        else:
           _ret[_key] = getattr(model,_key)
    return _ret

def init_db():
    sync_table(Users)
    sync_table(Role)
    sync_table(Session)
