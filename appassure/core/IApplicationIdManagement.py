"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class IApplicationIdManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IApplicationIdManagement
    """

    def getId(self):
        """Gets the core's ID."""
        return self.session.request('id/')
