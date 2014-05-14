"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ILocalizationManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ILocalizationManagement
    """

    def getAvailableCultures(self):
        """Gets a list of all available resource cultures."""
        return self.session.request('localization/availableCultures')

    def getCurrentCulture(self):
        """Gets the current resource culture."""
        return self.session.request('localization/currentCulture')

    def setCurrentCulture(self, lcid):
        """Sets new culture to all resources."""
        return self.session.request('localization/newCulture/%s'
                % (lcid), 'POST')
