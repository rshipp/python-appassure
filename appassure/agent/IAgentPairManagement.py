"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IAgentPairManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IAgentPairManagement
    """

    def pair(self, data):
        """Sets up relationship between a Core and the Agent
        including security certificates exchange.
        """
        return self.session.request('pair/', 'PUT',
                    self.getXML(data, 'agentPairingSettings'))

    def getPairingSettings(self):
        """Gets pairing settings of the Agent which includes
        agent ID, paired Core name and security certificate thumbprints.
        """
        return self.session.request('pair/')

    def removePairing(self):
        """Removes relationship between the Agent and a Core."""
        return self.session.request('pair/')

    def verifyConnect(self):
        """Allows to verify connection to specified agent and
        returns actual agent ID.
        """
        return self.session.request('pair/connect')

    def verifyConnectWithOptionalAuthentication(self, useNtlmOnly):
        """Allows to verify connection to specified agent with
        optional authentication scheme and returns actual agent ID.
        """
        return self.session.request('pair/connect/?useNtlmOnly=%s'
                % (useNtlmOnly))
