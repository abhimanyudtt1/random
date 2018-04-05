class modules (object):
    pass



for i in ['asdf'] :
    setattr(modules,'aads',__import__(i))

modules.aads = __import__('asdf')

print modules.aads.version


