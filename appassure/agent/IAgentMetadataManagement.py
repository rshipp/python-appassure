"""AppAssure 5 REST API"""

from appassure.appassureapi import AppAssureAPI

class IAgentMetadataManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IAgentMetadataManagement
    """

    def verifyCredentials(self, data):
        """Verifies specified credentials for MS Exchange and SQL
        servers.
        """
        return self.session.request('metadata/credentials', 'PUT',
                    self.getXML(data, 'credentialsDescriptor'))

    def getCurrentCluster(self, data):
        """Gets cached full metadata for the agent."""
        return self.session.request('metadata/fullClusterMetadata', 'PUT',
                    self.getXML(data, 'credentialsDescriptor'))

    def getCurrentClusterSummary(self, data):
        """Gets cached full metadata for the agent."""
        return self.session.request('metadata/fullClusterSummaryMetadata', 'PUT',
                    self.getXML(data, 'credentialsDescriptor'))

    def getCurrent(self, data):
        """Gets cached full metadata for the agent."""
        return self.session.request('metadata/fullMetadata', 'PUT',
                    self.getXML(data, 'credentialsDescriptor'))

    def getCurrentSummary(self, data):
        """Gets cached summary metadata for the agent with MS
        Exchange and SQL servers metadata.
        """
        return self.session.request('metadata/summaryMetadata', 'PUT',
                    self.getXML(data, 'credentialsDescriptor'))
