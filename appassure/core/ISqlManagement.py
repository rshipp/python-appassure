"""AppAssure 5 Core API"""

from appassure.api import AppAssureAPI

class ISqlManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/ISqlManagement
    """

    def verifyCredentials(self, data, agentId):
        """Verifies credentials to all SQL instances. Throws
        exception on validation failure for any instance.
        """
        return self.session.request('sql/agent/%s/verifySqlCredentials'
                % (agentId), 'PUT',
                    self.getXML(data, 'credentialsDescriptor'))

    def setAgentSqlSettings(self, data, agentId):
        """Sets agent-level sql settings."""
        return self.session.request('sql/agents/%s/sqlSettings'
                % (agentId), 'PUT',
                    self.getXML(data, 'agentSqlSettings'))

    def getAgentSqlSettings(self, agentId):
        """Gets agent-level sql settings."""
        return self.session.request('sql/agents/%s/sqlSettings'
                % (agentId))

    def setAttachabilitySettings(self, data):
        """Sets core-level attachability settings."""
        return self.session.request('sql/attachabilitySettings', 'PUT',
                    self.getXML(data, 'attachabilitySettings'))

    def getAttachabilitySettings(self):
        """Gets core-level attachability settings."""
        return self.session.request('sql/attachabilitySettings')

    def testSqlConnection(self, data):
        """Tests connection with instances of MSSQL servers
        installed on the Core and validates whether it would be
        possible to use those instances for attachability check.
        """
        return self.session.request('sql/connection', 'PUT',
                    self.getXML(data, 'sqlCredentials'))

    def forceAttachability(self, recoveryPointId):
        """Force attachability job for agent with given ID."""
        return self.session.request('sql/recoveryPoints/%s/force'
                % (recoveryPointId), 'POST')
