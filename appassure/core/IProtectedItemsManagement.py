"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IProtectedItemsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IProtectedItemsManagement
    """

    def getProtectedItems(self):
        """Gets the protected items tree."""
        return self.session.request('protectedItems/allItems')
