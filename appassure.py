"""Python wrapper for the AppAssure 5 REST API."""

import xml2obj
import requests
from requests_ntlm import HttpNtlmAuth

# AppAssure 5 API Core URL
API_URL = "apprecovery/api/core/"


class LoginError(Exception):
    """Connecting and/or logging in to the AppAssure server failed."""


class UnsupportedMethodError(Exception):
    """An unsupported HTTP method was specified."""


class InvalidURIError(Exception):
    """An invalid URI was specified."""


class Struct(dict):
    """Allows easy access to the parsed XML."""
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


def _xml2Obj(xml):
    """Return a structured object when given raw XML data."""
    obj = xml
    return obj

class AppAssureSession(object):
    """Allows us to request data from the API as a logged-in user."""
    
    def __init__(self, host, port, username, password, domain='DOMAIN'):
        self.host = host
        self.port = port
        self.username = username
        self.baseurl = "https://%s:%s/" % (host, port)
        self.apiurl = self.baseurl + API_URL
        self.loginurl = self.baseurl + 'apprecovery/admin/Core'
        self.http = requests.Session()
        self.auth = HttpNtlmAuth('%s\\%s' % (domain, self.username),
                password)
        status = self.http.get(self.loginurl, verify=False,
                auth=self.auth)
        if not status.ok:
            raise LoginError("Connecting and/or logging in to the AppAssure server failed.",
                   status)

    def __enter__(self):
        return self

    def close(self):
        """End the session."""
        self.http.close()

    def __exit__(self, type, value, tb):
        self.close()

    def request(self, uri, method='GET', data=None):
        """Sends a request to the AppAssure Core server, with the
           specified uri. Returns a structured object containing the
           data from the server's response. Method must be one of: GET,
           PUT, or POST. The optional 'data' parameter is only used if
           the HTTP method supports sending data to the server. (Eg,
           POST.)
        """
        if method == 'GET':
            response = self.http.get("%s%s" % (self.apiurl, uri),
                    auth=self.auth)
        elif method == 'POST':
            response = self.http.post("%s%s" % (self.apiurl, uri), data,
                    auth=self.auth)
        elif method == 'PUT':
            response = self.http.put("%s%s" % (self.apiurl, uri), data,
                    auth=self.auth)
        else:
            raise UnsupportedMethodError("Unsupported HTTP method", method)

        if response.ok:
            return xml2obj.xml2obj(response.text)
        else:
            raise InvalidURIError("The server returned an error message.",
                   response, self.apiurl + uri)


