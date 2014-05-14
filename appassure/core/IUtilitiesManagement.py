"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IUtilitiesManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IUtilitiesManagement
    """

    def getMachinesFromActiveDirectory(self, data):
        """Gets all machines from Active Directory."""
        return self.session.request('utilities/activeDirectoryMachines', 'POST',
                    self.getXML(data, 'getMachinesRequest'))

    def getMachinesFromActiveDirectoryByPage(self, data):
        """Gets machines by specific page from Active Directory."""
        return self.session.request('utilities/activeDirectoryMachinesByPage', 'POST',
                    self.getXML(data, 'getMachinesRequest'))

    def getDomainInfo(self, data):
        """Gets domain information."""
        return self.session.request('utilities/domainInformation', 'POST',
                    self.getXML(data, 'getDomainInfoRequest'))
