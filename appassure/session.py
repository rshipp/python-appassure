"""Python wrapper for the AppAssure 5 REST API.

Handles logging in to and sending and retrieving data from an
AppAssure server. Returns requested data as a Python object.
"""

from appassure.xml2obj import xml2obj
import requests
from requests_ntlm import HttpNtlmAuth

# AppAssure 5 API URLs
CORE_API_URL = "apprecovery/api/core/"
AGENT_API_URL = "apprecovery/api/agent/"
# Login URLs (any page that returns a 200 OK response when logged in)
CORE_LOGIN_URL = "apprecovery/admin/Core"
AGENT_LOGIN_URL = AGENT_API_URL + '/pair'
# Constants for both internal and external use
CORE = 'core'
AGENT = 'agent'


# Exception classes used by AppAssureSession.
class AppAssureError(Exception):
    """Base class for all AppAssure exception classes."""


class LoginError(AppAssureError):
    """Connecting and/or logging in to the AppAssure server failed."""


class UnsupportedMethodError(AppAssureError):
    """An unsupported HTTP method was specified."""


class InvalidURIError(AppAssureError):
    """An invalid URI was specified."""


class InvalidAPIError(AppAssureError):
    """And invalid API was specified."""


class AppAssureSession(object):
    """Allows us to request data from the API as a logged-in user."""

    def __init__(self, host, port, username, password, api=CORE, domain='DOMAIN'):
        """The default domain of 'DOMAIN' is used because this value is
        only relevant if you are authenticating against Active Directory.
        Be sure to set this to the appropriate value if you use Active
        Directory in your network.
        """
        self.username = username
        self.baseurl = "https://%s:%s/" % (host, port)
        if api == CORE:
            self.apiurl = self.baseurl + CORE_API_URL
            self.loginurl = self.baseurl + CORE_LOGIN_URL
        elif api == AGENT:
            self.apiurl = self.baseurl + AGENT_API_URL
            self.loginurl = self.baseurl + AGENT_LOGIN_URL
        else:
            raise InvalidAPIError("Valid API choices are '"+AGENT+"' and '"+CORE+"'.")
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
        """Sends a request to the AppAssure server, with the
        specified uri. Returns a structured object containing the
        data from the server's response. The optional 'data'
        parameter is only used if the HTTP method supports sending
        data to the server. (Eg, POST.)

        method must be one of:
            GET, POST, PUT, DELETE
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
        elif method == 'DELETE':
            response = self.http.delete("%s%s" % (self.apiurl, uri),
                    data, auth=self.auth)
        else:
            raise UnsupportedMethodError("Unsupported HTTP method", method)

        if response.ok:
            return xml2obj(response.text)
        else:
            raise InvalidURIError("The server returned an error message.",
                   response, self.apiurl + uri)
