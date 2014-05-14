"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class ILicenseManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ILicenseManagement
    """

    def getAgentLicenseInfo(self, agentId):
        """Gets licensing information for the given agent."""
        return self.session.request('license/agent/%s'
                % (agentId))

    def changeGroupKey(self, groupKey):
        """Gets new group key from the UI, validates it, and then
        returns the validation results.
        """
        return self.session.request('license/changeGroupKey/%s'
                % (groupKey), 'POST')

    def getCoreLicenseInfo(self):
        """Gets core licensing information."""
        return self.session.request('license/core')

    def isKeySpecifiedAndValid(self):
        """Gets state of the key."""
        return self.session.request('license/key')

    def getLicenseInfo(self):
        """Gets licensing information for Core and all the agents."""
        return self.session.request('license/licenseInfo')

    def getLicenseStatesNotifications(self):
        """Gets license states notifications for Core and all the
        agents.
        """
        return self.session.request('license/licenseStatesNotifications')

    def forcePhoneHome(self):
        """Forces connection with License Portal immediately."""
        return self.session.request('license/phoneHome/force', 'POST')

    def isPhoneHomeEnable(self):
        """Determines if the phone home operation is enabled."""
        return self.session.request('license/phoneHome/isEnable')

    def isPhoneHomeInProgress(self):
        """Determines if the phone home operation is in progress."""
        return self.session.request('license/phoneHome/isInProgress')
