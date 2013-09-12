"""Python wrapper for the AppAssure 5 REST API."""

import urllib
import urllib2
import httplib
import cookielib
import xml

API_URL = "apprecovery/api/core/"

def _xml2Obj(xml):
    """Return a structured object when given raw XML data."""

class AppAssureSession(object):
    """Allows us to request data from the API as a logged-in user."""
    
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.baseurl = "https://%s:%s/%s" % (host, port, API_URL)

