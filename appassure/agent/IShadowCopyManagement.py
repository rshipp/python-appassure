"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IShadowCopyManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IShadowCopyManagement
    """

    def getWriters(self):
        """Gets detailed information about Volume Shadow Copy
        Service (VSS) writers installed on the Agent.
        """
        return self.session.request('shadowcopy/writers/')
