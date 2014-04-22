"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class ICoreCallbackManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ICoreCallbackManagement
    """

    def processAgentProtectionRequest(self, data):
        """The method is called by failover agent in order to
        perform remote pairing. This method is for internal usage
        only.
        """
        return self.session.request('corecallback/agentprotectionrequest', 'POST',
                    self.getXML(data, 'coreCallbackRequest'))

    def verifyConnect(self):
        """Called by agent to verify connectivity to this core."""
        return self.session.request('corecallback/connect')
