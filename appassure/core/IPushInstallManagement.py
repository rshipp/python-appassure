"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IPushInstallManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IPushInstallManagement
    """

    def setConfiguration(self, data):
        """Sets PushInstall configuration."""
        return self.session.request('pushinstall/config', 'PUT',
                    self.getXML(data, 'pushInstallServiceConfig'))

    def getConfiguration(self):
        """Gets PushInstall configuration."""
        return self.session.request('pushinstall/config')

    def deployAgents(self, data):
        """Starts deploying agent(s) to remote machines."""
        return self.session.request('pushinstall/deployAgents', 'PUT',
                    self.getXML(data, 'pushInstallRequest'))

    def getDeployAgentVersion(self):
        """Get the version of the Agent to be deployed."""
        return self.session.request('pushinstall/deployAgentVersion')

    def getInstalledProducts(self, data):
        """Checks for already installed products."""
        return self.session.request('pushinstall/getInstalledProducts', 'POST',
                    self.getXML(data, 'machineInfo'))

    def getAgentServiceState(self, data):
        """Checks if agent is already installed on remote machine."""
        return self.session.request('pushinstall/isPushInstallNeed', 'POST',
                    self.getXML(data, 'machineInfo'))

    def isRemoveAgentProductRequired(self, removeProductId):
        """Checks whether removing of the Agent product is
        required. {installedProductVersion}.
        """
        return self.session.request('pushinstall/isRemoveAgentProductRequired/%s/'
                % (removeProductId))

    def validateMachine(self, data):
        """Checks machine availability and permissions for
        install agent.
        """
        return self.session.request('pushinstall/validateMachine', 'PUT',
                    self.getXML(data, 'machineInfo'))
