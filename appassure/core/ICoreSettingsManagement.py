"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class ICoreSettingsManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ICoreSettingsManagement
    """

    def getClientTimeout(self):
        """Gets timeout settings which are used in REST and
        socket communication.
        """
        return self.session.request('settings/clientTimeout')

    def setClientTimeout(self, data):
        """Applies timeout settings which are used in REST
        and socket communication.
        """
        return self.session.request('settings/clientTimeout', 'PUT',
                    self.getXML(data, 'clientTimeoutSettings'))

    def getCoreSettings(self):
        """Gets general global Core settings such as timeout
        settings and display name.
        """
        return self.session.request('settings/core')

    def setCoreSettings(self, data):
        """Applies general global Core settings such as
        timeout settings and display name.
        """
        return self.session.request('settings/core', 'PUT',
                    self.getXML(data, 'coreSettings'))

    def getCoreInstallPath(self):
        """Get path to a directory where Agent and Local
        Mount Utility installers are located.
        """
        return self.session.request('settings/installersPath')
