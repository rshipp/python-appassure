"""AppAssure 5 Core API"""

from appassure.appassureapi import AppAssureAPI

class IExchangeManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IExchangeManagement
    """

    def verifyCredentials(self, data, agentId):
        """Verifies credentials to Exchange instance. Throws 
        exception on validation failure.
        """
        return self.session.request('exchange/agent/%s/verifyExchangeCredentials' 
                % (agentId), 'PUT', 
                    self.getXML(data, 'baseCredentials'))

    def getAgentExchangeServerSettings(self, agentId):
        """Gets the exchange server settings for the agent."""
        return self.session.request('exchange/agents/%s/exchangeSettings' 
                % (agentId))

    def setAgentExchangeServerSettings(self, data, agentId):
        """Sets the exchange server settings for the agent."""
        return self.session.request('exchange/agents/%s/exchangeSettings' 
                % (agentId), 'PUT', 
                    self.getXML(data, 'exchangeServerSettings'))

    def forceChecksumCheck(self, recoveryPointId):
        """Forces checksum verification for the specified 
        recovery point.
        """
        return self.session.request('exchange/checksumcheck/%s/force' 
                % (recoveryPointId), 'POST')

    def getMountabilityQueueContents(self):
        """Gets the contents of the mountability queue."""
        return self.session.request('exchange/entries')

    def getMountabilityQueueEntry(self, entryid):
        """Gets the info for a specific moutability queue 
        entry.
        """
        return self.session.request('exchange/entries/%s' 
                % (entryid))

    def forceMountabilityCheck(self, recoveryPointId):
        """Forces mountability verification for the specified 
        recovery point.
        """
        return self.session.request('exchange/mountabilitycheck/%s/force' 
                % (recoveryPointId), 'POST')

    def getMountabilityQueueConfiguration(self):
        """Gets the configuration of the mountability queue."""
        return self.session.request('exchange/mountabilityConfig')

    def setMountabilityConfiguration(self, data):
        """Sets the configuration of the mountability queue."""
        return self.session.request('exchange/mountabilityConfig', 'POST', 
                    self.getXML(data, 'mountabilityConfiguration'))
