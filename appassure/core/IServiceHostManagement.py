"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IServiceHostManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=2294021
    """

    def getApiVersionInfo(self):
        """         Summary:."""
        return self.session.request('servicehost/apiVersion')

    def getConfiguration(self):
        """Gets current configuration of a server that listens
        for incoming REST calls.
        """
        return self.session.request('servicehost/config')

    def setConfiguration(self, data):
        """Sets current configuration of a server that listens
        for incoming REST calls.
        """
        return self.session.request('servicehost/config', 'POST',
                    self.getXML(data, 'serviceHostConfig'))

    def restart(self):
        """Immediately restarts a server that listens for
        incoming REST calls.
        """
        return self.session.request('servicehost/restart')

    def verifyConnection(self):
        """Allows to verify if listening server is configured
        properly and able to receive incoming REST calls.
        """
        return self.session.request('servicehost/verify')
