"""Python wrapper for the AppAssure 5 REST API.

   AppAssureAPI
   Provides an abstraction layer for using the AppAssure core API. Sends
   well-formed XML requests through a given AppAssureSession object.
"""

class AppAssureAPI(object):
    """Allows us to request data from the API as a logged-in user."""
    
    def __init__(self, session):
        """You MUST provide a valid AppAssureSession object as a
           parameter when creating a new AppAssureAPI object.
        """
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        """We don't want to close the AppAssureSession object, so there
           is nothing to do here.
        """
        pass

    def getXML(self, data, objname=None):
        """Convert a Python object into XML in the format expected by
           the AppAssure Core server. Uses self.data as input, and
           expects that imput to be a Python dictionary.

           Original source:
           http://code.activestate.com/recipes/440595-extensible-object-to-xml-convertor/
        """
        if type(data) == type({'':''}):
            # if data is a dict
            xml = "<%s>" % objname
            for key, value in data.items():
                xml += self.getXML(value, key)
            xml += "</%s>" % objname
        else:
            # assume data is a str
            xml = '<%s>%s</%s>' % (objname, data, objname)

        return ('<?xml version="1.0" encoding="utf-16"?>' +
                    xml).encode('utf-16')
