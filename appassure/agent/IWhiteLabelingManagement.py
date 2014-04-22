"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IWhiteLabelingManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IWhiteLabelingManagement
    """

    def getWhiteLabelingInfo(self):
        """Gets customizable strings."""
        return self.session.request('whitelabeling/whiteLabelingInfo')
