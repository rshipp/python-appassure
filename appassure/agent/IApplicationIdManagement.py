"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IApplicationIdManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/pages/viewpage.action?pageId=2294035
    """

    def getId(self):
        """Gets the core's ID."""
        return self.session.request('id/')
