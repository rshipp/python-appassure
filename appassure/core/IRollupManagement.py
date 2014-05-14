"""AppAssure 5 REST API"""

from appassure.api import AppAssureAPI

class IRollupManagement(AppAssureAPI):
    """Full documentation online at
    http://docs.appassure.com/display/AA50D/IRollupManagement
    """

    def getAgentRetentionPolicy(self, agentId):
        """Gets retention policy for a given agent ID."""
        return self.session.request('rollup/agents/%s'
                % (agentId))

    def setAgentRetentionPolicy(self, data, agentId):
        """Sets retention policy onto an agent with given ID."""
        return self.session.request('rollup/agents/%s'
                % (agentId), 'PUT',
                    self.getXML(data, 'agentRetentionPolicy'))

    def clearAgentRetentionPolicy(self, agentId):
        """Clears an agent's retention policy, and instead use
        the core-wide default one.
        """
        return self.session.request('rollup/agents/%s'
                % (agentId))

    def forceRollup(self, agentId):
        """Force rollup job for agent with given ID."""
        return self.session.request('rollup/agents/%s/force'
                % (agentId), 'POST')

    def getCoreRollupConfiguration(self):
        """Gets core rollup configuration."""
        return self.session.request('rollup/config')

    def setCoreRollupConfiguration(self, data):
        """Sets core rollup configuration."""
        return self.session.request('rollup/config', 'PUT',
                    self.getXML(data, 'rollupServiceConfig'))

    def getGranularityIntervals(self, data):
        """Gets granularity intervals for retention timeline."""
        return self.session.request('rollup/granularityIntervals', 'PUT',
                    self.getXML(data, 'getGranularityIntervalsRequest'))
