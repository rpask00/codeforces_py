import datetime as dt
import re

COMMON = {'blank':False, 'default':None}
CONFIG = {
    'CharField':     (str,         {'min_length':0,   'max_length':None}),
    'IntegerField':  (int,         {'min_value':None, 'max_value':None}),
    'BooleanField':  (bool,        {}),
    'DateTimeField': (dt.datetime, {'auto_now':False}),
    'EmailField':    (str,         {'min_length':0, 'max_length':None}),
}

class ValidationError(Exception):pass


class MetaField(type):
    def __new__(mcls,name,bases,dct):
        typ, constraints = CONFIG[name]
        constraints.update(COMMON)
        dct.update({ 'typ':typ, 'refKws':constraints })
        return type(name,bases+(Field,), dct)
        
        
class Field(object):
    def __init__(self,**kw):
        self.dct = {}
        dct = dict(self.refKws)
        for k,v in kw.items():  dct[k]=v
        for k,v in dct.items(): self.__dict__[k]=v
        self.__dict__['_def']=dct['default']
        
    def __set__(self,o,v): self.dct[o] = v
    def __get__(self,o,t=None): 
        o.__dict__                                   # <<< Strange thing...: without this, it doesn't work... :/ (doeans't pass the "not hasattr(User)" tets)
        return self.dct[o]
    
    def validate(f,o):    return f.validBlank(o) or f.validType(o)
    def validBlank(f,o):  return f.blank and f.dct[o] is None
    def validType(f,o):   return type(f.dct[o])==f.typ
    def validString(f,o): return f.validBlank(o) or (f.validType(o) and (f.min_length is None or f.min_length<=len(f.dct[o]))
                                                                    and (f.max_length is None or f.max_length>=len(f.dct[o])) )
    def validNumber(f,o): return f.validBlank(o) or (f.validType(o) and (f.min_value is None or f.min_value<=f.dct[o]) 
                                                                    and (f.max_value is None or f.dct[o]<=f.max_value) )
    
class BooleanField(metaclass=MetaField):pass
    
class CharField(metaclass=MetaField): 
    def validate(self,o): return self.validString(o)
        
class IntegerField(metaclass=MetaField):
    def validate(self,o): return self.validNumber(o)
    
class EmailField(metaclass=MetaField):
    def validate(self,o): return self.validBlank(o) or self.validString(o) and re.fullmatch(r'[a-z]+@[a-z]+\.[a-z]+', self.dct[o], flags=re.I)
        
class DateTimeField(metaclass=MetaField):
    def __get__(self,o,t=None):
        out = super().__get__(o,t)
        if self.auto_now and out is None: out = self.default
        return out
    @property
    def default(self): return self._def or self.auto_now and dt.datetime.now() or None
    @default.setter
    def default(self,v): self._def=v


class Model(object):
    def __init__(self,**kw):
        super().__init__()
        for fName,field in self.getFields():
            field.__set__(self, kw.get(fName,field.default))
            
    def validate(self):
        for fName,field in self.getFields():
            if not field.validate(self):
                raise ValidationError("Invalid field: "+fName)

    def getFields(self):
        return ( (fName,field) for fName,field in self.__class__.__dict__.items()
                                if isinstance(field,Field))
    

class User(Model):
    name = CharField()



u= User(name='daaaaaaaaaaaa')