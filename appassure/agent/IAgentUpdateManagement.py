"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IAgentUpdateManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IAgentUpdateManagement
    """

    def applyUpdate(self, data):
        """Performs automatic update of Agent service binaries.
        This method is for internal usage only and should not be called
        by users.
        """
        return self.session.request('update/', 'POST',
                    self.getXML(data, 'applyUpdateRequest'))
