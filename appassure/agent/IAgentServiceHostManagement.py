"""AppAssure 5 REST API"""

from appassure.appassureapi import AppAssureAPI

class IAgentServiceHostManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IAgentServiceHostManagement
    """

    def changePort(self, data):
        """Changes port number used by server which listens for
        incoming REST calls.
        """
        return self.session.request('agentServiceHost/port', 'POST',
                    self.getXML(data, 'agentPortChangeRequest'))
